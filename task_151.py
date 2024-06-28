import cv2
import numpy as np

logotype = np.zeros((500, 720, 3), 'uint8')

logotype[:] = 255, 255, 255
cv2.circle(logotype, (logotype.shape[0] // 2, logotype.shape[0] // 2),
           215, (235, 90, 140), thickness=5)
cv2.circle(logotype, (logotype.shape[0] // 2, logotype.shape[0] // 2),
           200, (235, 90, 140), thickness=5)
cv2.circle(logotype, (215, 310), 100, (235, 90, 140), thickness=5)
cv2.circle(logotype, (215, 310), 70, (235, 90, 140), thickness=5)
cv2.circle(logotype, (215, 310), 90, (235, 90, 140), thickness=5)
cv2.circle(logotype, (215, 310), 80, (235, 90, 140), thickness=5)
cv2.rectangle(logotype, (110, 140), (650, 315), (255, 255, 255), thickness=cv2.FILLED)
cv2.line(logotype, (115, 235), (115, 305), (235, 90, 140), thickness=5)
cv2.line(logotype, (125, 235), (125, 305), (235, 90, 140), thickness=5)
cv2.line(logotype, (135, 235), (135, 305), (235, 90, 140), thickness=5)
cv2.line(logotype, (145, 235), (145, 305), (235, 90, 140), thickness=5)
cv2.line(logotype, (285, 235), (285, 305), (235, 90, 140), thickness=5)
cv2.line(logotype, (295, 235), (295, 305), (235, 90, 140), thickness=5)
cv2.line(logotype, (305, 235), (305, 305), (235, 90, 140), thickness=5)
cv2.line(logotype, (315, 235), (315, 305), (235, 90, 140), thickness=5)
cv2.line(logotype, (115, 155), (115, 225), (235, 90, 140), thickness=5)
cv2.line(logotype, (125, 155), (125, 225), (235, 90, 140), thickness=5)
cv2.line(logotype, (135, 155), (135, 225), (235, 90, 140), thickness=5)
cv2.line(logotype, (145, 155), (145, 225), (235, 90, 140), thickness=5)
cv2.line(logotype, (285, 155), (285, 225), (235, 90, 140), thickness=5)
cv2.line(logotype, (295, 155), (295, 225), (235, 90, 140), thickness=5)
cv2.line(logotype, (305, 155), (305, 225), (235, 90, 140), thickness=5)
cv2.line(logotype, (315, 155), (315, 225), (235, 90, 140), thickness=5)
cv2.line(logotype, (115, 145), (145, 145), (235, 90, 140), thickness=5)
cv2.line(logotype, (285, 145), (315, 145), (235, 90, 140), thickness=5)
cv2.putText(logotype, 'RBAN', (325, 225), cv2.FONT_HERSHEY_TRIPLEX,3.5,
            (235, 90, 140), thickness=5)
cv2.putText(logotype, 'niversity', (325, 295), cv2.FONT_HERSHEY_TRIPLEX,2,
            (235, 90, 140), thickness=3)
cv2.putText(logotype, '2023', (192, 110), cv2.FONT_HERSHEY_DUPLEX,1.5,
            (235, 90, 140), thickness=5)
cv2.putText(logotype, 'Kazan', (470, 350), cv2.FONT_HERSHEY_TRIPLEX,1.5,
            (235, 90, 140), thickness=3)

cv2.imshow('Logotype', logotype)
cv2.waitKey(0)
