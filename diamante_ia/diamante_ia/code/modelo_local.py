from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Cargar modelo y tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

# Función mejorada con prompt guía y limpieza
def responder(input_text, max_tokens=100):
    prompt = f"Humano: {input_text}\nIA:"
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    with torch.no_grad():
        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=input_ids.shape[1] + max_tokens,
            do_sample=True,
            top_k=40,
            top_p=0.95,
            temperature=0.9,
            pad_token_id=tokenizer.eos_token_id
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Extraer solo la parte de IA
    if "IA:" in response:
        response = response.split("IA:")[1]
    return response.strip()
