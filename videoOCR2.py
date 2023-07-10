import cv2
import easyocr
import numpy as np

# Inisialisasi EasyOCR dengan model bahasa yang diinginkan
reader = easyocr.Reader(['en'])

# Buka video


detected_text = ""  # Variabel untuk menyimpan teks yang terdeteksi

while True:
    video = cv2.VideoCapture(0)
    # Baca frame video
    ret, frame = video.read()

    if not ret:
        break
    #potong = frame[150:720, 0:1280]

    # Ubah frame ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Baca teks dari frame
    results = reader.readtext(gray)

    # Tampilkan teks pada frame
    for result in results:
        bbox = result[0]
        text = result[1]

        # Gambar kotak di sekitar teks pada frame
        cv2.rectangle(frame, (int(bbox[0][0]), int(bbox[0][1])), (int(
            bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)

        # Tampilkan teks pada frame
        cv2.putText(frame, text, (int(bbox[0][0]), int(
            bbox[0][1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Tambahkan teks yang terdeteksi ke dalam string
        detected_text += text + " "

        # Cetak teks yang terdeteksi
        print("Teks yang terdeteksi:")
        print(detected_text)

    # Tampilkan frame dengan teks
    cv2.imshow('Video', frame)
    video = cv2.VideoCapture("videoparkir\parkir00.mp4")  # saran kholid

    # Hentikan jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Tutup video dan jendela
video.release()
cv2.destroyAllWindows()
