import unittest
from packages.core import SpeculativeEngine, SpeculativeTask, ValidationPipeline
from services.orchestrator import Orchestrator


class TestPipeline(unittest.TestCase):
    def test_orchestrator(self) -> None:
        task_queue = [SpeculativeTask(1, 'test', {})]
        validation_pipeline = ValidationPipeline('test', [])
        orchestrator = Orchestrator(task_queue, validation_pipeline)
        orchestrator.execute_tasks()
        self.assertEqual(orchestrator.get_execution_status(), 'Executed 1 tasks')