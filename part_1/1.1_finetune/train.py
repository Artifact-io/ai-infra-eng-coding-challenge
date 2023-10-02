from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
from datasets import load_dataset

MODEL_NAME = "roneneldan/TinyStories-28M"
DATASET_NAME = "b-mc2/sql-create-context"

def main():
	# Get the dataset and format the data for training
	dataset = load_dataset(DATASET_NAME, split="train")
	dataset = dataset.map(
		lambda examples: {"text": f"{examples['context']}\n{examples['question']}\n\n{examples['answer']}\n---"},
		batched=False,
		num_proc=4,
		remove_columns=dataset["train"].column_names,
	)

	# Train the model
	pass


if __name__ == "__main__":
	main()