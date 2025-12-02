import cv2
import numpy as np

# ---------------------------
# Konfigurasi HSV per warna
# ---------------------------

COLOR_RANGES = {
    "merah": [
        (np.array([0,   100, 100]), np.array([10,  255, 255])),
        (np.array([160, 100, 100]), np.array([179, 255, 255]))
    ],
    "hijau": [
        (np.array([35,  80,  80]),  np.array([85,  255, 255]))
    ],
    "biru": [
        (np.array([90,  80,  80]),  np.array([130, 255, 255]))
    ],
    "kuning": [
        (np.array([20,  80,  80]),  np.array([35,  255, 255]))
    ],
}

COLOR_ORDER = ["merah", "hijau", "biru", "kuning"]
COLOR_HUD_BGR = {
    "merah":   (0, 0, 255),
    "hijau":   (0, 255, 0),
    "biru":    (255, 0, 0),
    "kuning":  (0, 255, 255),
}

KERNEL_OPEN = np.ones((3, 3), np.uint8)
KERNEL_CLOSE = np.ones((5, 5), np.uint8)


def buat_mask_warna(hsv_frame, color_name):
    ranges = COLOR_RANGES[color_name]
    mask_total = np.zeros(hsv_frame.shape[:2], dtype=np.uint8)
    for lower, upper in ranges:
        mask_part = cv2.inRange(hsv_frame, lower, upper)
        mask_total = cv2.bitwise_or(mask_total, mask_part)
    return mask_total


def bersihkan_mask(mask):
    opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, KERNEL_OPEN, iterations=1)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, KERNEL_CLOSE, iterations=1)
    return closed


def anotasi_deteksi(frame, mask, color_name, min_area=1000):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    status = f"Tidak ada objek {color_name.upper()}"

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < min_area:
            continue

        x, y, w, h = cv2.boundingRect(cnt)
        cx = x + w // 2
        cy = y + h // 2

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)

        h_frame, w_frame = frame.shape[:2]
        if cx < w_frame / 3:
            pos = "LEFT"
        elif cx > 2 * w_frame / 3:
            pos = "RIGHT"
        else:
            pos = "CENTER"

        status = f"{color_name.upper()} DETECTED ({pos})"
        cv2.putText(frame, status, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 255, 0), 2, cv2.LINE_AA)

    return frame, status


def main():
    # pakai CAP_DSHOW biar lebih stabil di Windows
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("Gagal membuka kamera.")
        return

    cv2.namedWindow("Frame")
    cv2.resizeWindow("Frame", 960, 720)

    active_mode = -1           # -1 = no detection, 0..3 = index COLOR_ORDER
    show_mask_overlay = True
    mask_scale = 0.4           # ukuran awal mask (0.1 s/d 0.8 kira-kira)

    print("=== Kontrol Keyboard ===")
    print("1 : deteksi MERAH")
    print("2 : deteksi HIJAU")
    print("3 : deteksi BIRU")
    print("4 : deteksi KUNING")
    print("0 : non-aktifkan deteksi (hanya frame asli)")
    print("M : show/hide overlay mask")
    print("[ : kecilkan mask")
    print("] : besarkan mask")
    print("Q : keluar")
    print("========================")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        display = frame.copy()
        status_text = "Mode: tidak ada deteksi"
        color_name = None
        mask = None

        if 0 <= active_mode < len(COLOR_ORDER):
            color_name = COLOR_ORDER[active_mode]
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = buat_mask_warna(hsv, color_name)
            mask = bersihkan_mask(mask)

            display, status_text = anotasi_deteksi(display, mask, color_name)

        # HUD teks
        cv2.putText(display, status_text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (255, 255, 255), 2, cv2.LINE_AA)

        controls_text = "1:R  2:G  3:B  4:Y  0:OFF  M:Mask  [:Mask-  ]:Mask+  Q:Quit"
        cv2.putText(display, controls_text,
                    (10, display.shape[0] - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                    (255, 255, 255), 1, cv2.LINE_AA)

        # HUD warna aktif
        if color_name is not None:
            color_bgr = COLOR_HUD_BGR[color_name]
            h_box, w_box = 30, 60
            x1 = display.shape[1] - w_box - 10
            y1 = 10
            x2 = x1 + w_box
            y2 = y1 + h_box
            cv2.rectangle(display, (x1, y1), (x2, y2), color_bgr, -1)
            cv2.putText(display, color_name[0].upper(), (x1 + 18, y1 + 22),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 0, 0), 2, cv2.LINE_AA)

        # Overlay mask (picture-in-picture) dengan ukuran bisa diatur
        if show_mask_overlay and mask is not None:
            mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

            # hitung ukuran berdasarkan scale
            frame_h, frame_w = display.shape[:2]
            w_small = int(frame_w * mask_scale)
            # jaga rasio aspek sama dengan frame
            h_small = int(w_small * frame_h / frame_w)

            mask_small = cv2.resize(mask_bgr, (w_small, h_small))

            x1 = frame_w - w_small - 10
            y1 = 50
            x2 = x1 + w_small
            y2 = y1 + h_small

            display[y1:y2, x1:x2] = mask_small
            cv2.putText(display, "Mask", (x1 + 5, y1 + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow("Frame", display)

        key = cv2.waitKey(1) & 0xFF

        if key in (ord('q'), ord('Q')):
            break
        elif key in (ord('1'), ord('2'), ord('3'), ord('4')):
            active_mode = int(chr(key)) - 1
            print(f"Mode diubah ke: deteksi {COLOR_ORDER[active_mode].upper()}")
        elif key == ord('0'):
            active_mode = -1
            print("Deteksi dinonaktifkan (hanya frame asli).")
        elif key in (ord('m'), ord('M')):
            show_mask_overlay = not show_mask_overlay
            print(f"Overlay mask: {'ON' if show_mask_overlay else 'OFF'}")
        elif key == ord('['):       # kecilkan mask
            mask_scale = max(0.1, mask_scale - 0.05)
            print(f"Mask scale: {mask_scale:.2f}")
        elif key == ord(']'):       # besarkan mask
            mask_scale = min(0.8, mask_scale + 0.05)
            print(f"Mask scale: {mask_scale:.2f}")

    cap.release()
    cv2.destroyAllWindows()
    print("Program selesai.")


if __name__ == "__main__":
    main()
