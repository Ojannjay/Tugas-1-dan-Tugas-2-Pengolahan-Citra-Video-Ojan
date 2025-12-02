"""
Tugas 1 - Blurring & Sharpening (Webcam)

Fitur:
- Mode filter:
    0 : Normal (tanpa filter)
    1 : Average Blur 5x5
    2 : Average Blur 9x9
    3 : Gaussian Blur 5x5
    4 : Sharpen
- HUD: nama filter aktif + bantuan kontrol di bagian bawah frame
"""

import cv2
import numpy as np

# ---------------------------
# Definisi kernel & mode
# ---------------------------

# Average blur 5x5 dan 9x9
KERNEL_AVG_5 = np.ones((5, 5), np.float32) / (5 * 5)
KERNEL_AVG_9 = np.ones((9, 9), np.float32) / (9 * 9)

# Gaussian blur 5x5 (bikin kernel sendiri)
g1d = cv2.getGaussianKernel(ksize=5, sigma=1.0)
KERNEL_GAUSS_5 = g1d @ g1d.T  # 5x5

# Kernel sharpening
KERNEL_SHARPEN = np.array([[0, -1,  0],
                           [-1, 5, -1],
                           [0, -1,  0]], dtype=np.float32)

FILTER_LABELS = {
    0: "Normal",
    1: "Average Blur 5x5",
    2: "Average Blur 9x9",
    3: "Gaussian Blur 5x5",
    4: "Sharpen",
}


# ---------------------------
# Fungsi bantu
# ---------------------------

def apply_filter(frame, mode):
    """Terapkan filter sesuai mode dan kembalikan (frame_hasil, label)."""
    if mode == 1:
        out = cv2.filter2D(frame, -1, KERNEL_AVG_5)
    elif mode == 2:
        out = cv2.filter2D(frame, -1, KERNEL_AVG_9)
    elif mode == 3:
        out = cv2.filter2D(frame, -1, KERNEL_GAUSS_5)
    elif mode == 4:
        out = cv2.filter2D(frame, -1, KERNEL_SHARPEN)
    else:
        out = frame.copy()

    label = FILTER_LABELS.get(mode, "Unknown")
    return out, label


# ---------------------------
# Program utama
# ---------------------------

def main():
    # Pakai CAP_DSHOW biar lebih stabil di Windows
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("Gagal membuka kamera.")
        return

    cv2.namedWindow("Tugas 1 - Blurring & Sharpening")
    cv2.resizeWindow("Tugas 1 - Blurring & Sharpening", 960, 720)

    mode = 0  # default: normal

    print("=== Kontrol Keyboard ===")
    print("0 : Normal")
    print("1 : Average Blur 5x5")
    print("2 : Average Blur 9x9")
    print("3 : Gaussian Blur 5x5")
    print("4 : Sharpen")
    print("Q : keluar")
    print("========================")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        # Terapkan filter
        filtered, label = apply_filter(frame, mode)

        # HUD: nama filter aktif di atas
        cv2.putText(filtered, f"Filter: {label}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255, 255, 255), 2, cv2.LINE_AA)

        # HUD: bantuan kontrol di bawah
        controls_text = "0:Normal  1:Avg5  2:Avg9  3:Gauss5  4:Sharpen  Q:Quit"
        cv2.putText(filtered, controls_text,
                    (10, filtered.shape[0] - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1, cv2.LINE_AA)

        cv2.imshow("Tugas 1 - Blurring & Sharpening", filtered)

        key = cv2.waitKey(1) & 0xFF
        if key in (ord('q'), ord('Q')):
            break
        elif key in (ord('0'), ord('1'), ord('2'), ord('3'), ord('4')):
            mode = int(chr(key))
            print(f"Mode diubah ke: {FILTER_LABELS[mode]}")

    cap.release()
    cv2.destroyAllWindows()
    print("Program selesai.")


if __name__ == "__main__":
    main()
