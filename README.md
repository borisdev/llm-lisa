# llm-error-clusters

The objective here is to detect patterns in LLM output errors.

This might be useful for two reasons:

-   make more nuanced performance comparisons between models
-   make more strategic decisions in feeding high impact examples to fine-tune a LLM

The approach I will take is to port work aleady down in exploratory spatial
data analysis to the LLM domain. The idea is to use clustering algorithms to
group similar errors together, and then label them to make them interpretable.

## Appendix -- Very rough notes to self -- 3 candidate datasets source???

### DATA 1: LLM Arena - ELO rating -- head to head battles

#### basic idea with this data

% wins on the question
see where % wins on question and question type are correlated
name clusters

https://github.com/lm-sys/FastChat/blob/main/docs/dataset_release.md
https://huggingface.co/datasets/lmsys/mt_bench_human_judgments/viewer/default/human?p=4
https://lmarena.ai/?leaderboard
Code to reproduce the leaderboard:
https://colab.research.google.com/drive/1KdwokPjirkTmpO_P1WByFNFiqxWQquwH

#### Data 2: Hugging Face, Open LLM Leaderboard v2 Data

the main open-llm-leaderboard/contents is an aggregation of the open-llm-leaderboard-old/results.

dataset contains per-model result files (JSON) with detailed outputs across tasks.

#### Data 3: Hugging Face, Open LLM Leaderboard v2 Data

https://huggingface.co/datasets/open-llm-leaderboard/results

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

LOOK AT THIS!!!!

https://github.com/VILA-Lab/Open-LLM-Leaderboard?utm_source=chatgpt.com

MMLU-Pro
https://huggingface.co/blog/wolfram/llm-comparison-test-2025-01-02
https://huggingface.co/blog/wolfram/llm-comparison-test-2024-12-04

MTEB (Massive Text Embedding Benchmark):
https://huggingface.co/blog/mteb

https://huggingface.co/docs/leaderboards/open_llm_leaderboard/archive

## IMDB Dataset Example

```python

Dataset({
    features: ['text', 'label'],
    num_rows: 250
})
{
    'text': 'I rented I AM CURIOUS-YELLOW from my video store because of all the controversy that surrounded it when
it was first released in 1967. I also heard that at first it was seized by U.S. customs if it ever tried to enter
this country, therefore being a fan of films considered "controversial" I really had to see this for myself.<br /><br
/>The plot is centered around a young Swedish drama student named Lena who wants to learn everything she can about
life. In particular she wants to focus her attentions to making some sort of documentary on what the average Swede
thought about certain political issues such as the Vietnam War and race issues in the United States. In between
asking politicians and ordinary denizens of Stockholm about their opinions on politics, she has sex with her drama
teacher, classmates, and married men.<br /><br />What kills me about I AM CURIOUS-YELLOW is that 40 years ago, this
was considered pornographic. Really, the sex and nudity scenes are few and far between, even then it\'s not shot like
some cheaply made porno. While my countrymen mind find it shocking, in reality sex and nudity are a major staple in
Swedish cinema. Even Ingmar Bergman, arguably their answer to good old boy John Ford, had sex scenes in his films.<br
/><br />I do commend the filmmakers for the fact that any sex shown in the film is shown for artistic purposes rather
than just to shock people and make money to be shown in pornographic theaters in America. I AM CURIOUS-YELLOW is a
good film for anyone wanting to study the meat and potatoes (no pun intended) of Swedish cinema. But really, this
film doesn\'t have much of a plot.',
    'label': 0
}
```
