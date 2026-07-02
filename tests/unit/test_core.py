import unittest
from packages.core import SpeculativeEngine, SpeculativeTask, ValidationPipeline


class TestCore(unittest.TestCase):
    def test_speculative_engine_init(self) -> None:
        task_queue = [SpeculativeTask(1, 'test', {})]
        validation_pipeline = ValidationPipeline('test', [])
        engine = SpeculativeEngine(task_queue, validation_pipeline)
        self.assertIsNotNone(engine)

    def test_execute_task(self) -> None:
        task_queue = [SpeculativeTask(1, 'test', {})]
        validation_pipeline = ValidationPipeline('test', [])
        engine = SpeculativeEngine(task_queue, validation_pipeline)
        result = engine.execute_task(task_queue[0])
        self.assertTrue(result)