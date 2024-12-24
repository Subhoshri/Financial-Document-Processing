import pytesseract
from PIL import Image
import boto3

def extract_text_with_tesseract(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image, lang='eng+kor')

def extract_text_with_textract(image_path):
    client = boto3.client('textract')
    with open(image_path, 'rb') as file:
        response = client.analyze_document(
            Document={'Bytes': file.read()},
            FeatureTypes=['FORMS']
        )
    return ''.join([block['Text'] for block in response['Blocks'] if block['BlockType'] == 'LINE'])

def extract_text(image_path, engine='tesseract'):
    if engine == 'tesseract':
        return extract_text_with_tesseract(image_path)
    elif engine == 'aws':
        return extract_text_with_textract(image_path)
    else:
        raise ValueError("Unsupported OCR engine")
