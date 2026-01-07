import pytesseract
from d4compare.ocr.preprocess import preprocess

def ocr_image(pil_image):
    processed = preprocess(pil_image)
    text = pytesseract.image_to_string(processed, lang="eng")
    return text
