from packages.core.types import KnowledgeGraph, InputData
from packages.core.engine import ReasoningEngine


class Orchestrator:
    def __init__(self, knowledge_graph: KnowledgeGraph):
        self.engine = ReasoningEngine(knowledge_graph)

    def ingest_data(self, input_data: InputData):
        self.engine.ingest_data(input_data)

    def reason(self):
        return self.engine.reason()