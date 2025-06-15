from PySide6.QtWidgets import (
    QFileDialog, QLabel, QPushButton, QVBoxLayout,
    QWidget, QMessageBox, QTextEdit, QHBoxLayout, QSizePolicy
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
from PIL.ImageQt import ImageQt
from model.detector import PPEInferencer
from utils.compliance import analyze_compliance


class PPEApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🛡️ PPE Compliance Checker")
        self.setFixedSize(900, 700)

        # Model initialization
        self.model = PPEInferencer("weights/best.onnx")

        # Image display label
        self.image_label = QLabel("📷 Please upload an image", alignment=Qt.AlignCenter)
        self.image_label.setFixedSize(640, 480)
        self.image_label.setStyleSheet("border: 2px dashed #aaa;")
        self.image_label.setScaledContents(True)

        # Compliance result display
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setFont(QFont("Consolas", 10))
        self.result_display.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
        self.result_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Button
        self.upload_button = QPushButton("📂 Select Image")
        self.upload_button.setFont(QFont("Arial", 10, QFont.Bold))
        self.upload_button.setStyleSheet("padding: 10px 20px;")
        self.upload_button.clicked.connect(self.load_image)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.upload_button, alignment=Qt.AlignCenter)
        layout.addWidget(QLabel("🧾 Compliance Summary:", alignment=Qt.AlignLeft))
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg *.jpeg)")
        if file_path:
            try:
                img, class_list = self.model.detect(file_path)
                qt_img = ImageQt(img)
                pixmap = QPixmap.fromImage(qt_img)
                self.image_label.setPixmap(pixmap)

                compliance_stats = analyze_compliance(class_list)
                result_str = "\n".join([f"{k}: {v}" for k, v in compliance_stats.items()])
                self.result_display.setPlainText(result_str)
            except Exception as e:
                QMessageBox.critical(self, "Detection Error", str(e))
        else:
            QMessageBox.warning(self, "No Image", "No image was selected.")