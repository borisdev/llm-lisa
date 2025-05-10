# llm-error-clusters

## Hugging Face Open‐LLM‐Leaderboard Datasets

the main open-llm-leaderboard/contents is an aggregation of the open-llm-leaderboard-old/results.

dataset contains per-model result files (JSON) with detailed outputs across tasks.

```python

from datasets import load_dataset
contents = load_dataset("open-llm-leaderboard/contents", split="train")
results = load_dataset("open-llm-leaderboard/results", split="train")
```

The results dataset organizes data by model name and timestamp. Each JSON file includes aggregated metrics and typically the individual question prompts, model outputs, and true labels for tasks like MMLU, HellaSwag, ARC, etc.

This allows you to extract raw predictions and compare against ground truth. (For example, inspecting a model’s file shows fields like "doc_to_text", "doc_to_target" or "target" indicating the true answer and the model’s answer.) See the HF dataset pages for file download links or the HF Hub to pull data via code.

Per-model JSON outputs: In open-llm-leaderboard/results, each model-folder contains results\_\*.json files (as on Hugging Face) with the model’s predictions. These can be downloaded directly or fetched via datasets.load_dataset.
