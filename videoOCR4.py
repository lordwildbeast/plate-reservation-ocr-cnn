import cv2
import easyocr
import time

# Inisialisasi EasyOCR
reader = easyocr.Reader(['en'])

# Inisialisasi video dari file atau webcam
# Ganti dengan path file video, atau 0 untuk webcam
video = cv2.VideoCapture(0)

# Inisialisasi variabel waktu
start_time = time.time()

while True:
    # Baca frame dari video
    ret, frame = video.read()

    # Ubah frame ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi teks menggunakan EasyOCR
    results = reader.readtext(gray)

    # Tampilkan teks yang terdeteksi pada frame
    for result in results:
        bbox = result[0]
        text = result[1]

        # Gambar kotak di sekitar teks pada frame
        cv2.rectangle(frame, (int(bbox[0][0]), int(bbox[0][1])), (int(
            bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)

        # Tampilkan teks pada frame
        cv2.putText(frame, text, (int(bbox[0][0]), int(
            bbox[0][1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Tampilkan frame
    cv2.imshow('Video', frame)

    # Cetak teks yang terdeteksi setiap 5 detik
    elapsed_time = time.time() - start_time
    if elapsed_time >= 5:
        detected_texts = [result[1] for result in results]
        print(f'Detected Texts: {", ".join(detected_texts)}')
        start_time = time.time()

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup video dan jendela tampilan
video.release()
cv2.destroyAllWindows()
