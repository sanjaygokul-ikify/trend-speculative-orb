import argparse
from typing import List
from packages.core.types import SpeculativeTask, ValidationPipeline
from services.orchestrator import Orchestrator


def main() -> None:
    parser = argparse.ArgumentParser(description='Speculative execution runtime')
    parser.add_argument('--tasks', type=str, help='List of tasks to execute')
    parser.add_argument('--pipeline', type=str, help='Validation pipeline')
    args = parser.parse_args()

    task_queue: List[SpeculativeTask] = []
    validation_pipeline = ValidationPipeline('default', [])

    orchestrator = Orchestrator(task_queue, validation_pipeline)
    orchestrator.execute_tasks()
    print(orchestrator.get_execution_status())