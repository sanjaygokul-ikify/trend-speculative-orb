import unittest
from packages.utils import logging


class TestRuntime(unittest.TestCase):
    def test_setup_logger(self) -> None:
        logger = logging.setup_logger('test')
        self.assertIsNotNone(logger)