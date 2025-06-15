# 🦺 PPE Detection Desktop App

A lightweight desktop application for detecting **Personal Protective Equipment (PPE)** like helmets and vests using a deep learning model. It features a drag-and-drop GUI and uses **YOLOv8 + ONNX** for real-time image inference.

---

## 🧠 Machine Learning Model

This app uses **YOLOv8 (You Only Look Once, version 8)** for object detection. The model is:

- Trained using the **Ultralytics YOLOv8 framework**
- Exported to **ONNX format** for fast inference with **ONNX Runtime**
- Suitable for detecting multiple PPE items (helmet, vest, etc.) in a single image

**Advantages**:
- ⚡ Real-time performance  
- 🧩 Small model size  
- 📦 Easy to package with Python

---

## 📂 Project Structure
PPE-Detection-App/
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
│   ├── file_loader.py    # Folder/image loading
│   └── compliance.py     # Safety rule checker
├── requirements.txt
└── ppe_app.spec          # (Auto-generated) for PyInstaller

![image](https://github.com/user-attachments/assets/aed58308-eb18-4ece-9f3e-6e439380a143)


