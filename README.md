# Titles

-   Local Hotspot Detection for LLM Evaluation with Getis–Ord G\*

# Comparing LLMs with LISAs

LISA stands for [Local Indicators of Spatial Association](https://onlinelibrary.wiley.com/doi/10.1111/j.1538-4632.1995.tb00338.x).

# What's spatial association?

Spatial association in terms of language models refers semantic association
using high dimensional embedding vectors.

# Why local?

Examples of local concerns in LLM performance evaluation are as follows:

-   Which LLM is least socially biased?
-   Which LLM is best with medical answers?
-   Which LLM is least likely to produce toxic content?
-   Which LLM produces more nuanced, and less over confident, simplistic answers?

A LISA (a local indicator) might reveal big variation in high priority local concerns that aggregate performance metrics hide.

The objective here is to detect local hot spots in LLM performance variation.

Practically, this might be useful for two reasons:

-   revealing local patterns of performance gives model users information to make more nuanced performance comparisons between models that are more directly relevant to their specific user priority concerns.
-   revealing local patterns of performance gives model developers information to make more strategic decisions in feeding high impact examples to fine-tune a LLM

## Approach

### LISA (Local Indicators of Spatial Association)

The approach I will take is to port work already done in exploratory spatial
data analysis to the LLM domain -- more specifically work on local indicators
of spatial association ([Local Indicators of Spatial Association—LISA](https://onlinelibrary.wiley.com/doi/10.1111/j.1538-4632.1995.tb00338.x)).

### basic idea with using LLM Arena's ELO data

-   get % battle wins for each model for each question
-   see where % wins on 'clustered questions' are correlated
-   use LLM to name these clusters
-   write a report on the patterns...disaggregate, more nuanced performance comparisons

## Data source: LLM Arena - ELO rating -- head to head battles

-   https://github.com/lm-sys/FastChat/blob/main/docs/dataset_release.md
-   https://huggingface.co/datasets/lmsys/mt_bench_human_judgments/viewer/default/human?p=4
-   https://lmarena.ai/?leaderboard
-   Code to reproduce the leaderboard, https://colab.research.google.com/drive/1KdwokPjirkTmpO_P1WByFNFiqxWQquwH

## Question -- maybe this data might be better ?

https://github.com/VILA-Lab/Open-LLM-Leaderboard?utm_source=chatgpt.com
