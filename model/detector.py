from ultralytics import YOLO
import cv2

class PPEInferencer:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, image_path, conf=0.3):
        img = cv2.imread(image_path)
        results = self.model.predict(img, conf=conf)[0]
        return results.plot(), results.boxes.cls.tolist()
