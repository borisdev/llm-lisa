"""
Example of loading and processing datasets using the `datasets` library.

Check out Huggingface MCP server for more datasets?
"""

import logging

from datasets import load_dataset, load_dataset_builder
from huggingface_hub import list_datasets
from rich import print

logging.basicConfig(level=logging.DEBUG)


# Load a small subset of the IMDb dataset
dataset = load_dataset("imdb", split="train[:1%]")  # Loads 1% of the training data

# Print some examples
print(dataset)
print(dataset[0])
# https://github.com/VILA-Lab/Open-LLM-Leaderboard?utm_source=chatgpt.com
benchmark_name = "Open-Style/Open-LLM-Benchmark"
gpt4_outputs = load_dataset("Open-Style/Open-LLM-Benchmark", "gpt4")
print(f"Benchmark: {benchmark_name}")
print(gpt4_outputs)

gpt4_outputs = load_dataset("Open-Style/Open-LLM-Benchmark", "gpt4")
print(gpt4_outputs)
#
# print([dataset.id for dataset in list_datasets()])
#
# ds_builder = load_dataset_builder("cornell-movie-review-data/rotten_tomatoes")
# print(ds_builder.info.description)
#


def main(inp):
    return f"Hello, {inp}!"


# # Load a dataset and print the first example in the training set
# squad_dataset = load_dataset("rajpurkar/squad")
# print(squad_dataset["train"][0])
#
# # Process the dataset - add a column with the length of the context texts
# dataset_with_length = squad_dataset.map(lambda x: {"length": len(x["context"])})
# print(dataset_with_length)
