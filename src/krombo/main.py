#!/usr/bin/env python
import sys
import warnings

from krombo.crew import Krombo

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "0x28fb66a9259ba21ba1c97f8fb99195ced1811a23706966c244eaea7ed9acc4e5",
        "blockchain_name": "Aptos"
        
    }
    Krombo().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "0x629e7Da20197a5429d30da36E77d06CdF796b71A",
        "blockchain_name": "Ethereum"
    }
    try:
        Krombo().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Krombo().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "0x629e7Da20197a5429d30da36E77d06CdF796b71A",
        "blockchain_name": "Ethereum"
    }
    try:
        Krombo().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
