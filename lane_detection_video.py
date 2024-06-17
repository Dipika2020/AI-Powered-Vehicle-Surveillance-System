import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

cap = cv2.VideoCapture('road_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny_frame = cv2.Canny(gray_frame, 100, 200)

    height, width = frame.shape[:2]
    region_of_interest_vertices = [(0, height), (width / 2, height / 2), (width, height)]
    cropped_frame = region_of_interest(canny_frame, np.array([region_of_interest_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped_frame, rho=6, theta=np.pi / 180, threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=25)
    frame_with_lines = draw_the_lines(frame, lines)

    cv2.imshow('Lane Detection', frame_with_lines)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
