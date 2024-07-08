import cv2 as cv

video_path = r'E:\aHieu\video\Grey Modern Professional Business Project Presentation (3).mp4'

cap = cv.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        print("error: Could not read frame")
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
    cv.imshow('gray', gray)

cap.release()
cv.destroyAllWindows()