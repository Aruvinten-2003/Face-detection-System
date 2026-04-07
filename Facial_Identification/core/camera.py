import cv2

class Camera:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(camera_index)

        def is_opened(self):
            return self.cap.isOpened()
        
        def read_frame(self):
            return self.cap.read()

        def release(self):
            if self.cap:
                self.cap.release()
