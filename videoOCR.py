import cv2
import easyocr

# Inisialisasi EasyOCR dengan model bahasa yang diinginkan
reader = easyocr.Reader(['en'])

# ocr_result = reader.readtext(1)
# print(ocr_result)

# Buka video
# hikvision: rtsp://admin:labai123@192.168.1.64:554/Streaming/Channels/101
video = cv2.VideoCapture(
    "rtsp://admin:labai123@192.168.1.64:554/Streaming/Channels/101")

detected_text = ""  # Variabel untuk menyimpan teks yang terdeteksi

while video.isOpened():
    # Baca frame video
    ret, frame = video.read()

    if not ret:
        break

    # Ubah frame ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Baca teks dari frame
    results = reader.readtext(gray)

    # Tampilkan teks pada frame

    for result in results:
        # Ambil posisi kotak teks
        bbox = result[0]
        # Ambil teks
        text = result[1]

        # Gambar kotak di sekitar teks
        cv2.rectangle(frame, (int(bbox[0][0]), int(bbox[0][1])), (int(
            bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)

        # Tampilkan teks
        cv2.putText(frame, text, (int(bbox[0][0]), int(
            bbox[0][1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    for result in results:
        text = result[1]
        detected_text += text + " "

    # Tampilkan frame dengan teks
    cv2.imshow('Video', frame)

    # Hentikan jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):  # cv2.waitKey() jika sumber dari gambar
        break

# Cetak teks yang terdeteksi
print("Teks yang terdeteksi:")
print(detected_text)

# Tutup video dan jendela
video.release()
cv2.destroyAllWindows()
