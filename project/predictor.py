import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# model_path = 'project/models'
model_path = 'mahima18/qat5'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

def generate_question(text, model=model, tokenizer=tokenizer, max_length=64):    # Encode the text input ensuring padding and truncation
    input_ids = tokenizer.encode("context: " + text, return_tensors="pt", max_length=512, padding="max_length", truncation=True).to(model.device)
    output_ids = model.generate(input_ids, max_length=max_length, num_beams=4, early_stopping=True)

    # Decode the output to text
    question = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    print('Question',question)
    return question

