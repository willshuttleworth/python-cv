import pytesseract
import cv2 as cv

cap = cv.VideoCapture('scale.avi')

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        print("no more frames, exiting")
        break
    
    # if frame is read correctly ret is True
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = img[800:1050, 400:950]
    blur = cv.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    target = pytesseract.image_to_string(th3, lang='eng', config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789').strip()
    target = target[:len(target) - 1] + '.' + target[len(target) - 1:]
    print(target)
cap.release()
