🧠 AI图像识别网页
本项目是一个结合深度学习与前端交互的图像识别系统，支持用户上传图片并由训练好的模型检测图片是否由AI生成。

📁 项目结构
AI-Image-Theme-Detection-Web
├── best_model.pth          # 训练好的PyTorch模型文件          
├── templates/
│   └── index.html              # 前端页面模板
├── app.py                      # Flask 后端接口，处理图片上传与模型预测
├── model.ipynb                 # 训练模型的代码
├── dataset/                    
│ ├── train/
│ │     ├── real/
│ │     └── ai/
│ ├── val/
│ │     ├── real/
│ │     └── ai/
│ └── test/
│       ├── real/
│       └── ai/               #数据集
└── README.md                   # 项目说明文档

🚀 快速开始
1. 安装依赖
     
2. 安装模型（较快）/训练模型
   二者选其一：
   （1）安装模型：请在 [Releases 页面](https://github.com/你的用户名/你的项目名/releases) 下载训练好的模型文件 `best_model.pth` 并放入项目根目录。
   （2）训练模型：自己在网上寻找图片按照上面的项目结构放置图片，然后运行model.ipynb

3. 运行项目
python app.py
默认服务运行于 http://127.0.0.1:5000

4. 上传图片并获取识别结果
通过网页上传任意图片，即可获得AI返回的主题标签。

🧠 模型说明
本项目使用卷积神经网络（CNN）在自定义图像主题数据集上进行训练。
