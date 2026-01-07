import mss
from PIL import Image

# TEMP: hard-coded tooltip region
# You will replace this with calibration later
CAPTURE_REGION = {
    "top": 300,
    "left": 900,
    "width": 600,
    "height": 700
}

def capture_tooltip():
    with mss.mss() as sct:
        try:
            shot = sct.grab(CAPTURE_REGION)
        except Exception:
            return None

        img = Image.frombytes("RGB", shot.size, shot.rgb)
        return img
