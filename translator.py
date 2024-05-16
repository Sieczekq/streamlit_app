from transformers import MarianTokenizer, TFMarianMTModel

def translate(text, model_name="Helsinki-NLP/opus-mt-en-de"):
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = TFMarianMTModel.from_pretrained(model_name)

    inputs = tokenizer.encode(text, return_tensors="tf", padding=True)

    translated = model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
    
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return translated_text
