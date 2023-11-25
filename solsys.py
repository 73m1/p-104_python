import cv2

img = cv2.imread("solar-system.jpg")
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.putText(img,
        "Sun",
        (30,100),
           fontFace =cv2.FONT_HERSHEY_COMPLEX,
           fontScale =0.5,  
           color =(255,255,255)
        )
cv2.putText(img,
        "Mercury",
        (70,130),
           fontFace =cv2.FONT_HERSHEY_COMPLEX,
           fontScale =0.5,  
           color =(255,255,255)
        )
cv2.putText(img,
        "venus",
        (100,60),
           fontFace =cv2.FONT_HERSHEY_COMPLEX,
           fontScale =0.5,  
           color =(255,255,255)
        )
cv2.putText(img,
        "earth",
        (145,140),
           fontFace =cv2.FONT_HERSHEY_COMPLEX,
           fontScale =0.5,  
           color =(255,255,255)
        )
cv2.putText(img,
        "Mars",
        (190,70),
           fontFace =cv2.FONT_HERSHEY_COMPLEX,
           fontScale =0.5,  
           color =(255,255,255)
        )
cv2.putText(img,
        "Jupiter",
        (240,100),
           fontFace =cv2.FONT_HERSHEY_COMPLEX,
           fontScale =0.5,  
           color =(255,255,255)
        )
cv2.putText(img,
        "saturn",
        (350,50),
            fontFace =cv2.FONT_HERSHEY_COMPLEX,
           fontScale =0.5,  
           color =(255,255,255)
        )
cv2.putText(img,
        "Uranus",
        (460,50),
            fontFace =cv2.FONT_HERSHEY_COMPLEX,
           fontScale =0.5,  
           color =(255,255,255)
        )
cv2.putText(img,
        "Neptune",
        (530,50),
            fontFace =cv2.FONT_HERSHEY_COMPLEX,
           fontScale =0.5,  
           color =(255,255,255)
        )

cv2.imwrite("Solar_Systemwithname.jpg",img)