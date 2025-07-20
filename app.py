from flask import Flask, request, jsonify, render_template
from PIL import Image
import torch
from torchvision import models
import torchvision.transforms as transforms
import io

# 初始化 Flask
app = Flask(__name__)

# 加载模型（用你训练好的模型路径）
# 实例化模型
model = models.resnet18(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = torch.nn.Sequential(
    torch.nn.Dropout(0.5),          # Dropout 概率可以调，例如 0.3~0.5
    torch.nn.Linear(num_ftrs, 2)
)
# 加载权重
model.load_state_dict(torch.load('best_model.pth'))
# 设置为评估模式
model.eval()

# 类别标签
class_names = ['AI', 'Real']

# 图像预处理
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})

    file = request.files['file']
    image = Image.open(file.stream).convert('RGB')
    image = transform(image).unsqueeze(0)  # [1, 3, 128, 128]

    with torch.no_grad():
        outputs = model(image)
        probs = torch.nn.functional.softmax(outputs[0], dim=0)
        prob_list = probs.tolist()
        predicted_idx = torch.argmax(probs).item()
        predicted_class = class_names[predicted_idx]
    
    return jsonify({
        'predicted_class': predicted_class,
        'probabilities': {
            'AI': round(prob_list[0], 3),
            'Real': round(prob_list[1], 3)
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
