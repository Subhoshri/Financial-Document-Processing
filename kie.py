from transformers import LayoutLMv3Processor, LayoutLMv3ForTokenClassification
from PIL import Image
import torch

# Load model and processor
processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base")
model = LayoutLMv3ForTokenClassification.from_pretrained("microsoft/layoutlmv3-base")

def extract_key_value_pairs(image_path):
    image = Image.open(image_path)
    encoding = processor(image, return_tensors="pt")
    outputs = model(**encoding)
    predictions = torch.argmax(outputs.logits, dim=-1)

    tokens = processor.tokenizer.convert_ids_to_tokens(encoding.input_ids[0])
    key_values = {tokens[i]: predictions[0][i].item() for i in range(len(tokens))}
    return key_values
