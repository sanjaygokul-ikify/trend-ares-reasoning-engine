from typing import Dict, List
from dataclasses import dataclass

@dataclass
class InputData:
    data: List[int]

@dataclass
class KnowledgeGraph:
    data: Dict[str, str] = None

    def __post_init__(self):
        if self.data is None:
            self.data = {}

    def add(self, item: str) -> None:
        self.data[item] = item

class ReasoningResult:
    def __init__(self, result: Dict[str, str]):
        self.result = result

    def get_result(self) -> Dict[str, str]:
        return self.result
