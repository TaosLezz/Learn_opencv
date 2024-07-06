import cv2

img_path = r'E:\aHieu\pictures\op_face_crop.jpg'
video_path = r'E:\aHieu\video\Grey Modern Professional Business Project Presentation (3).mp4'
def rescaling_frame(frame, scale = 0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)


img = cv2.imread(img_path)
resize_img = rescaling_frame(img)
cv2.imshow('img', img)
cv2.imshow('resize img', resize_img)
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        print(('error: could not read frame'))
    resize_frame = rescaling_frame(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('resize_frame', resize_frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()