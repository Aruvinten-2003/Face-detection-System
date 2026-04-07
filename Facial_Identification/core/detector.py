import cv2
import mediapipe as mp

class FaceDetector:
    def __init__(self, min_detection_confidence=0.5):
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=min_detection_confidence)


    def detect_faces(self,frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_detection.process(rgb_frame)
        return results
    
    def draw_detections(self, frame, results):
        face_count = 0
        h, w, _ = frame.shape

        if results.detections:
            face_count = len(results.detections)

            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                box_width = int(bbox.width * w)
                box_height = int(bbox.height * h)

                x = max(0, x)
                y = max(0, y)

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + box_width, y + box_height),
                    (0, 255, 0),
                    2
                )

                confidence = detection.score[0] * 100
                label = f"Face {confidence:.1f}%"

                cv2.putText(
                    frame,
                    label,
                    (x, y - 10 if y - 10 > 20 else y + 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

        cv2.putText(
            frame,
            f"Faces Found: {face_count}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        return frame


