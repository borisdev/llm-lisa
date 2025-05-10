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

#### basic idea with using LLM Arena's ELO data

-   get % battle wins for each model for each question
-   see where % wins on 'clustered questions' are correlated
-   use LLM to name these clusters
-   write a report on the patterns...disaggregate, more nuanced performance comparisons

#### Data source: LLM Arena - ELO rating -- head to head battles

-   https://github.com/lm-sys/FastChat/blob/main/docs/dataset_release.md
-   https://huggingface.co/datasets/lmsys/mt_bench_human_judgments/viewer/default/human?p=4
-   https://lmarena.ai/?leaderboard
-   Code to reproduce the leaderboard, https://colab.research.google.com/drive/1KdwokPjirkTmpO_P1WByFNFiqxWQquwH

## Question -- maybe this data might be better ?

https://github.com/VILA-Lab/Open-LLM-Leaderboard?utm_source=chatgpt.com
