import cv2
import numpy as np
import easyocr
import time


# Inisialisasi EasyOCR dengan model bahasa yang diinginkan
reader = easyocr.Reader(['en'], gpu=True)

# Inisialisasi variabel waktu awal
start_time = time.time()
frame_count = 0

while True:
    # Inisialisasi video dari webcam
    video = cv2.VideoCapture("videoparkir\parkir00.mp4")

    # Baca frame dari video
    ret, frame = video.read()

    if not ret:
        break
    # crop video dengan lebar dari 150px - 720px, dan tinggi 0px - 1280px
    potong = frame[150:720, 0:1280]

    # Ubah frame ke greyscale
    gray = cv2.cvtColor(potong, cv2.COLOR_BGR2GRAY)

    # Baca teks dari frame
    results = reader.readtext(gray)

    # Tampilkan teks pada frame
    for result in results:
        # Ambil posisi kotak teks
        bbox = result[0]
        # Ambil teks
        text = result[1]

        # Gambar kotak di sekitar teks
        cv2.rectangle(potong, (int(bbox[0][0]), int(bbox[0][1]), int(
            bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)

        # Tampilkan teks
        cv2.putText(potong, text, (int(bbox[0][0]), int(
            bbox[0][1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    '''
    # Buat persegi menggunakan array NumPy
    square = np.array(
        [[100, 100], [400, 100], [400, 400], [100, 400]], np.int32)
    square = square.reshape((-1, 1, 2))

    # Gambar persegi pada frame
    cv2.polylines(frame, [square], True, (0, 255, 0), thickness=2)
    '''

    # Tampilkan FPS
    frame_count += 1
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time
    cv2.putText(potong, f'FPS: {fps:.2f}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Tampilkan frame
    cv2.imshow('Cyberpunk 2099', potong)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup video dan jendela tampilan
video.release()
cv2.destroyAllWindows()
