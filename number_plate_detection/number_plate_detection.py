import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import pytesseract
from pytesseract import Output

def detect_number_plate(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(bfilter, 30, 200)
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    location = None

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break

    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2 + 1, y1:y2 + 1]

    ret, thresh1 = cv2.threshold(cropped_image, 210, 255, cv2.THRESH_BINARY)
    img1 = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    d = pytesseract.image_to_data(img1, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img1 = cv2.rectangle(cropped_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    extracted_text = pytesseract.image_to_string(img1, lang='eng')
    return extracted_text

if __name__ == "__main__":
    image_path = "number_plate_images/car_img1.jpg"
    print(detect_number_plate(image_path))
