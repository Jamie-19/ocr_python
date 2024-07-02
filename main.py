from PIL import Image
import pytesseract
from image import image_conv

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image_path = 'test.jpeg'
new_path =image_conv(image_path)
image = Image.open(new_path)
text = pytesseract.image_to_string(image)
output_text = 'output.txt'
with open(output_text, 'w', encoding='utf-8') as file:
    file.write(text)

