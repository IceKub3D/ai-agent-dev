import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import torch

# Synthetic dataset (replace with real data like IMDb if available)
data = {
    "text": [
        "This movie was fantastic, loved every moment!",
        "Terrible film, really boring and poorly acted.",
        "An amazing experience, great plot and characters!",
        "Disappointing, the story was weak and unengaging.",
        "Absolutely wonderful, a must-watch for everyone!"
    ],
    "label": [1, 0, 1, 0, 1]  # 1: Positive, 0: Negative
}
dataset = Dataset.from_dict(data)

# Load pretrained BERT model and tokenizer
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Tokenize dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_dataset = dataset.map(tokenize_function, batched=True)
train_dataset = tokenized_dataset.train_test_split(test_size=0.2)["train"]
eval_dataset = tokenized_dataset.train_test_split(test_size=0.2)["test"]

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

# Fine-tune the model
trainer.train()

# Test the agent on sample reviews
test_reviews = [
    "This movie was incredible, highly recommend it!",
    "Awful, I couldn't stand watching it."
]
inputs = tokenizer(test_reviews, padding=True, truncation=True, return_tensors="pt")
outputs = model(**inputs)
predictions = torch.argmax(outputs.logits, dim=1)
for review, pred in zip(test_reviews, predictions):
    label = "Positive" if pred == 1 else "Negative"
    print(f"Review: {review}\nPrediction: {label}\n")