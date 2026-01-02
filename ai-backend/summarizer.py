from transformers import BartTokenizer, BartForConditionalGeneration
import torch

MODEL_NAME = "facebook/bart-large-cnn"

tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)

def generate_summary(text: str) -> str:
    if not text or len(text.strip()) == 0:
        return ""

    # Tokenize with HARD limit (this prevents the crash)
    inputs = tokenizer(
        text,
        max_length=1024,          # 🔥 BART LIMIT
        truncation=True,
        return_tensors="pt"
    )

    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=150,
            min_length=50,
            do_sample=False
        )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
