from .image_processor import ImageProcessor
from .file_handler import process_file
from .llm import process_text

class CodeReview:
    def __init__(self):
        self.image_processor = ImageProcessor()

    def analyze(self, content):
        if content.endswith('.py'):  # Обработка текстового файла
            return process_file(content)
        else:  # Обработка изображения
            extracted_text = self.image_processor.extract_text(content)
            return process_text(extracted_text)

