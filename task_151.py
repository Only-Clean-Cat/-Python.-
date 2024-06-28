import cv2
import numpy as np

logotype_color = np.zeros((500, 720, 3), 'uint8')
for i in range(720):
    color = int(255*i/720)
    cv2.line(logotype_color, (i,720), (i, 0), (color, color, color), thickness=1)

cv2.ellipse(logotype_color, (230,250),(215,215),0,15,327,(235, 90, 140),thickness=5)
cv2.ellipse(logotype_color, (230,250),(200,200),0,17,325,(235, 90, 140),thickness=5)
cv2.ellipse(logotype_color, (215,310),(100,100),0,3,177,(235, 90, 140),thickness=5)
cv2.ellipse(logotype_color, (215,310),(90,90),0,4,176,(235, 90, 140),thickness=5)
cv2.ellipse(logotype_color, (215,310),(80,80),0,4,176,(235, 90, 140),thickness=5)
cv2.ellipse(logotype_color, (215,310),(70,70),0,4,176,(235, 90, 140),thickness=5)
cv2.line(logotype_color, (115, 235), (115, 305), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (125, 235), (125, 305), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (135, 235), (135, 305), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (145, 235), (145, 305), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (285, 235), (285, 305), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (295, 235), (295, 305), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (305, 235), (305, 305), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (315, 235), (315, 305), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (115, 155), (115, 225), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (125, 155), (125, 225), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (135, 155), (135, 225), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (145, 155), (145, 225), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (285, 155), (285, 225), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (295, 155), (295, 225), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (305, 155), (305, 225), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (315, 155), (315, 225), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (115, 145), (145, 145), (235, 90, 140), thickness=5)
cv2.line(logotype_color, (285, 145), (315, 145), (235, 90, 140), thickness=5)
cv2.putText(logotype_color, 'RBAN', (325, 225), cv2.FONT_HERSHEY_TRIPLEX,3.5,
            (235, 90, 140), thickness=5)
cv2.putText(logotype_color, 'niversity', (325, 295), cv2.FONT_HERSHEY_TRIPLEX,2,
            (235, 90, 140), thickness=3)
cv2.putText(logotype_color, '2023', (172, 110), cv2.FONT_HERSHEY_DUPLEX,1.5,
            (235, 90, 140), thickness=5)
cv2.putText(logotype_color, 'Kazan', (470, 350), cv2.FONT_HERSHEY_TRIPLEX,1.5,
            (235, 90, 140), thickness=2)

cv2.imshow('Logotype', logotype_color)
cv2.waitKey(0)
