import cv2
faseCascade = cv2.CascadeClassifier("face/haarcascade_frontalface_default.xml")
noseCascade = cv2.CascadeClassifier("face/Nariz.xml")

bw_threshold = 80

video_capture = cv2.VideoCapture(0)
mask_on = False

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    wajah = faseCascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in wajah:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        if mask_on:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(frame, 'Mask On', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
        hidung = noseCascade.detectMultiScale(roi_gray, 1.18, 35,)
        for (sx, sy, sw, sh) in hidung:
            cv2.rectangle(roi_color, (sh, sy), (sx+sw, sy+sh), (255, 0, 0), 2)
            cv2.putText(frame, 'Hidung', (x + sx, y + sy),
                        1, 1, (0, 255, 0), 1)
        if len(hidung) > 0:
            mask_on = False
        else:
            mask_on = True

    cv2.putText(frame, 'Jumlah Wajah :' + str(len(wajah)),
                (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Deteksi Masker', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
