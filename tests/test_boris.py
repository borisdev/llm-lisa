from datasets import \
    load_dataset  # HuggingFace community-driven open-source library of datasets

from llm_error_clusters.main import main


def test_main():
    test_input = "World"
    actual_output = main(test_input)
    expected_output = f"Hello, {test_input}!"

    # Assert that the actual output matches the expected output
    assert (
        actual_output == expected_output
    ), f"Expected: {expected_output}, but got: {actual_output}"


def test_data():
    # HuggingFace community-driven open-source library of datasets
    contents = load_dataset("open-llm-leaderboard/contents", split="train")
    results = load_dataset("open-llm-leaderboard/results", split="train")
    print(contents)
    print(results)
    breakpoint()
