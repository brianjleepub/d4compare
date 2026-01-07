import sys
import keyboard
from PyQt6.QtWidgets import QApplication

from d4compare.capture.screenshot import capture_tooltip
from d4compare.ocr.engine_tesseract import ocr_image
from d4compare.ui.toast import show_toast

def on_hotkey():
    image = capture_tooltip()
    if image is None:
        show_toast("ERROR", "No capture region set")
        return

    text = ocr_image(image)
    preview = text[:300].strip() or "(no text detected)"
    show_toast("OCR CAPTURED", preview)

def main():
    app = QApplication(sys.argv)

    keyboard.add_hotkey("ctrl+shift+x", on_hotkey)

    show_toast("d4compare", "Ready — Ctrl+Shift+X")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
