from sklearn.model_selection import train_test_split
from transformers import Trainer, TrainingArguments

def active_learning_feedback(new_data, model, tokenizer):
    train_data, test_data = train_test_split(new_data, test_size=0.2)

    training_args = TrainingArguments(
        output_dir='./results',
        evaluation_strategy="epoch",
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_data,
        eval_dataset=test_data,
        tokenizer=tokenizer
    )
    trainer.train()
