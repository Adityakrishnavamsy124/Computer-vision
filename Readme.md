📦 PPE-Detection-App/
│
├── main.py               # Entry point for GUI
├── gui/                  # UI elements
│   ├── layout.ui         # (Optional) designed in Qt Designer
│   └── controller.py     # Logic to connect GUI + model
├── model/
│   └── detector.py       # YOLOv8 ONNX inference wrapper
├── weights/
│   └── best.onnx         # Your trained ONNX model
├── utils/
│   └── file_loader.py    # Folder/image loading
│   └── compliance.py     # Safety rule checker
├── requirements.txt
└── ppe_app.spec          # (Auto-generated) for PyInstaller


GUI	PySide6 / PyQt6	Desktop interface, drag-drop, views
Detection	Ultralytics + ONNX	Efficient YOLOv8 ONNX inference
Image	OpenCV	Drawing boxes, reading frames
Packaging	PyInstaller	Turn Python into .exe

![image](https://github.com/user-attachments/assets/aed58308-eb18-4ece-9f3e-6e439380a143)


