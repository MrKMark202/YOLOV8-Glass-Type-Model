from ultralytics import YOLO
import cv2

model = YOLO("./best.pt")

video_putanja = './data/test/videos/casa.mp4'
cap = cv2.VideoCapture(video_putanja)

# Dobij trenutne dimenzije frejma
width = int(cap.get(3))
height = int(cap.get(4))

# Proveri dimenzije prvog frejma
ret, frame = cap.read()
print(frame.shape)

# Kreiraj VideoWriter objekat
output_putanja = './data/test/videos/casa_output.avi'
# Probaj sa različitim fourcc vrednostima
fourcc_options = ['XVID', 'MJPG', 'H264']
fourcc = None

for option in fourcc_options:
    fourcc = cv2.VideoWriter_fourcc(*option)
    out = cv2.VideoWriter(output_putanja, fourcc, 20.0, (width, height))
    if out.isOpened():
        break

if not out.isOpened():
    raise Exception("Nije moguće otvoriti izlazni video.")

ret = True

while ret:
    ret, frame = cap.read()

    # Provjeri jesu li dimenzije frejma ispravne
    if not ret or frame is None:
        break

    # Dodaj ovu liniju za promenu dimenzija frejma
    frame = cv2.resize(frame, (width, height))

    results = model.track(frame, persist=True)

    frame_ = results[0].plot()

    cv2.imshow('Frame', frame_)  # Koristi cv2_imshow umesto cv2.imshow
    out.write(frame_)   # Dodaj frejm u izlazni video

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Oslobodi resurse
cap.release()
out.release()
cv2.destroyAllWindows()