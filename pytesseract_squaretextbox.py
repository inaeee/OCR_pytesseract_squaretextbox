import cv2
import pytesseract
from pytesseract import Output

img=cv2.imread("C:\\Users\\inaee\\Desktop\\2020-1MAKERS\\OCR\\square_size500\\gray\\square_gray_3.jpg")

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)


#d=pytesseract.image_to_data(img, output_type=Output.DICT)
#print(d.keys())

#n_boxes=len(d['text'])
#for i in range(n_boxes):
#    if int(d['conf'][i]) > 60:
#        (x,y,w,h)=(d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#        img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

#cv2.imshow('img',img)
#print(d['text'])
#cv2.imwrite("C:\\Users\\inaee\\Desktop\\2020-1MAKERS\\OCR\\명함\\textbox\\square_text_1.jpg", img)
#cv2.waitKey(0)
