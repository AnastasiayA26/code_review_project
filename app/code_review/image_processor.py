from PIL import Image
import pytesseract

class ImageProcessor:
    def __init__(self):
        self.tesseract_cmd = '/usr/bin/tesseract'

    def extract_text(self, image_path):
        """
        Извлекает текст из изображения с помощью OCR.
        """
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image, config='--psm 6')
            return text
        except Exception as e:
            print(f"Ошибка обработки изображения: {e}")
            return ''

