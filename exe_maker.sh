pyinstaller main.py \
--add-data "weights/best.onnx:weights" \
--hidden-import=onnxruntime \
--hidden-import=ultralytics \
--hidden-import=ultralytics.models.yolo \
--hidden-import=cv2