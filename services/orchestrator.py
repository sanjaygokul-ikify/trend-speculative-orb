from typing import List
from packages.core.types import SpeculativeTask, ValidationPipeline
from packages.core import SpeculativeEngine


class Orchestrator:
    def __init__(self, task_queue: List[SpeculativeTask], validation_pipeline: ValidationPipeline):
        self.task_queue = task_queue
        self.validation_pipeline = validation_pipeline
        self.engine = SpeculativeEngine(task_queue, validation_pipeline)

    def execute_tasks(self) -> None:
        for task in self.task_queue:
            self.engine.execute_task(task)

    def get_execution_status(self) -> str:
        return self.engine.get_execution_status()