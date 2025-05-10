# llm-error-clusters

The objective here is to detect patterns in LLM output errors.

This might be useful for two reasons:

-   make more nuanced performance comparisons between models
-   make more strategic decisions in what types of example to use for fine-tuning

The approach I will take is to port work aleady down in exploratory spatial
data analysis to the LLM domain. The idea is to use clustering algorithms to
group similar errors together, and then label them to make them interpretable.

## Appendix -- Very rough notes to self

#### Hugging Face, Open LLM Leaderboard v2 Data

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

### List the top Arxiv papers on detecting patterns in the errors of different LLM on huggingface benchmark tests?

1. Evaluating LLMs at Detecting Errors in LLM Responses
   Authors: Ryo Kamoi et al.

Published: April 2024

Summary: This paper introduces ReaLMistake, a benchmark designed to evaluate LLMs' ability to detect errors in their own responses. It categorizes errors into four types: reasoning correctness, instruction-following, context-faithfulness, and parameterized knowledge. The study finds that even top-tier models like GPT-4 and Claude 3 struggle with error detection, often performing worse than humans.
arXiv
+1
ar5iv
+1

https://arxiv.org/abs/2404.03602?utm_source=chatgpt.com

https://github.com/psunlpgroup/ReaLMistake
https://huggingface.co/datasets/ryokamoi/realmistake

3. Benchmarking LLMs via Uncertainty Quantification
   Authors: Fanghua Ye et al.

Published: January 2024

Summary: This study emphasizes the importance of incorporating uncertainty quantification in LLM evaluations. It reveals that models with higher accuracy may exhibit lower certainty and that larger-scale LLMs can display greater uncertainty. The paper suggests that current evaluation platforms, like Hugging Face's Open LLM Leaderboard, should integrate uncertainty measures for a more comprehensive assessment.

https://arxiv.org/abs/2401.12794?utm_source=chatgpt.com
