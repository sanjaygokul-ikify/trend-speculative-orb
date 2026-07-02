from typing import Dict, List
from dataclasses import dataclass

@dataclass
class SpeculativeTask:
    id: int
    name: str
    data: Dict

@dataclass
class ValidationPipeline:
    name: str
    steps: List[str]