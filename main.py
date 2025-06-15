import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QFileDialog, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QImage
from ultralytics import YOLO
from utils.compliance import check_compliance

# ✅ Load the ONNX model via ultralytics
model = YOLO("weights/best.onnx")  # not ort, this works like on Kaggle

class PPEApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PPE Detection with YOLO ONNX")
        self.resize(900, 700)

        self.image_label = QLabel("Upload an image to check PPE compliance")
        self.image_label.setFixedSize(800, 500)
        self.image_label.setStyleSheet("border: 2px solid gray;")
        self.image_label.setScaledContents(True)

        self.button = QPushButton("Upload Image")
        self.button.clicked.connect(self.load_image)

        self.result_label = QLabel("Result: ")
        self.result_label.setStyleSheet("font-size: 14px;")

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            results = model(file_path)[0]
            img = cv2.imread(file_path)

            # Draw detections
            for box in results.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                label = f"{model.names[cls]} {conf:.2f}"
                color = (0, 255, 0)
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                cv2.putText(img, label, (x1, max(y1 - 5, 0)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Compliance check
            class_ids = [int(box.cls[0]) for box in results.boxes]
            stats = check_compliance(class_ids)
            self.show_image(img)

            result_text = "\n".join([f"{k}: {v}" for k, v in stats.items()])
            self.result_label.setText(result_text)

    def show_image(self, img):
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qimg = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(qimg))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PPEApp()
    window.show()
    sys.exit(app.exec())
