from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer

def show_toast(title, message, duration=3500):
    toast = QWidget()
    toast.setWindowFlags(
        Qt.WindowType.FramelessWindowHint |
        Qt.WindowType.Tool |
        Qt.WindowType.WindowStaysOnTopHint
    )

    layout = QVBoxLayout()
    title_label = QLabel(f"<b>{title}</b>")
    msg_label = QLabel(message)

    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    msg_label.setWordWrap(True)

    layout.addWidget(title_label)
    layout.addWidget(msg_label)

    toast.setLayout(layout)
    toast.resize(420, 220)
    toast.show()

    QTimer.singleShot(duration, toast.close)
