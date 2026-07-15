from typing import List
from packages.core.engine import SpeculativeEngine
from packages.core.types import SpeculativeTask

class Executor:
    def __init__(self, task_queue: List[SpeculativeTask]):
        self.task_queue = task_queue
        self.engine = SpeculativeEngine(task_queue, None)

    def execute(self) -> bool:
        for task in self.task_queue:
            try:
                if not self.engine.handle_timeout(task, 10.0):
                    raise Exception(f"Task {task.id} timed out")
                self.engine.execute_task(task)
            except Exception as e:
                print(f"Error executing task {task.id}: {str(e)}")
        return True