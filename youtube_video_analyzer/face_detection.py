import cv2
import os
import json


class FaceDetection:
    def __init__(self, folder_path, output_file):
        self.folder_path = folder_path
        self.output_file = output_file
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_alt.xml"
        )
        self.results = []
        print(self.face_cascade)

    def detect_faces(self):
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                self.process_image(filename)
        self.save_results()

    def process_image(self, filename):
        image_path = os.path.join(self.folder_path, filename)
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        self.collect_results(filename, faces)

    def collect_results(self, filename, faces):
        image_results = {
            "image_frame": filename,
            "num_faces": len(faces),
            "faces": [
                {"x": int(x), "y": int(y), "width": int(w), "height": int(h)}
                for (x, y, w, h) in faces
            ],
        }
        self.results.append(image_results)

    def save_results(self):
        with open(self.output_file, "w") as f:
            json.dump(self.results, f, indent=4)
