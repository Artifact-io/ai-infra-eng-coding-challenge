import os
from typing import List

from transformers import (
	AutoTokenizer,
	AutoModelForCausalLM
)
import torch
from pydantic import BaseModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MODEL_PATH = os.environ.get("MODEL_PATH")

model = AutoModelForCausalLM.from_pretrained(MODEL_PATH).to(device)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

class Instance(BaseModel):
	question: str
	context: str

def get_predictions(instances: List[Instance]) -> List[str]:
	instances = [ f"{instance.context}\n{instance.question}\n\n" for instance in instances ]
	inputs = tokenizer(instances, return_tensors="pt").input_ids.to(device)
	outputs = model.generate(inputs, max_new_tokens=200, do_sample=True, top_k=50, top_p=0.95)

	predictions = tokenizer.batch_decode(outputs[:, inputs.shape[1]:], skip_special_tokens=True)

	predictions = [ p.split("---")[0].strip() for p in predictions ]

	return predictions

# Implement an HTTP service to make inference predictions.