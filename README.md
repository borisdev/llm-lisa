# Detecting Local Patterns in LLM Performance Battles

The objective here is to detect local patterns in LLM performance.

This might be useful for two reasons:

-   revealing local patterns of performance gives model users information to make more nuanced performance comparisons between models that are more directly relevant to their specific user priority concerns.
-   revealing local patterns of performance gives model developers information to make more strategic decisions in feeding high impact examples to fine-tune a LLM

The approach I will take is to port work already done in exploratory spatial
data analysis to the LLM domain -- more specifically work on local indicators
of spatial association (LISAs).

## References:

-   [Local Indicators of Spatial Association—LISA](https://onlinelibrary.wiley.com/doi/10.1111/j.1538-4632.1995.tb00338.)

## Miscellaneous notes

Elo Uncovered: Robustness and Best Practices in Language Model Evaluation
https://arxiv.org/abs/2311.17295

Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference
https://arxiv.org/html/2403.04132v1

am-ELO: A Stable Framework for Arena-based LLM Evaluation
https://www.arxiv.org/pdf/2505.03475#

_TextClass Benchmark: A Continuous Elo Rating of LLMs in Social Sciences_
Author: Bastián González-Bustamante
Published: November 30, 2024
Summary: This work introduces the TextClass Benchmark, an ongoing evaluation framework that employs a tailored Elo rating system to assess LLMs on text classification tasks across various social science domains and languages. The benchmark updates ratings continuously, incorporating new models and test sets to evaluate generalization capabilities.
https://arxiv.org/abs/2412.00539?utm_source=chatgpt.com
https://github.com/bgonzalezbustamante/TextClass-Benchmark
https://textclass-benchmark.com/

-   [Elo rating of local contextual patterns](https://colab.ws/articles/10.1109%2FCCDC.2011.5968634)

#### Data source: LLM Arena - ELO rating -- head to head battles

#### basic idea with this data

-   get % battle wins for each model for each question
-   see where % wins on 'clustered questions' are correlated
-   use LLM to name these clusters
-   write a report on the patterns...disaggregate, more nuanced performance comparisons

https://github.com/lm-sys/FastChat/blob/main/docs/dataset_release.md
https://huggingface.co/datasets/lmsys/mt_bench_human_judgments/viewer/default/human?p=4
https://lmarena.ai/?leaderboard
Code to reproduce the leaderboard:
https://colab.research.google.com/drive/1KdwokPjirkTmpO_P1WByFNFiqxWQquwH

## LOOK AT THIS!!!!

https://github.com/VILA-Lab/Open-LLM-Leaderboard?utm_source=chatgpt.com
