import unittest
from packages.core.types import KnowledgeGraph, InputData
from services.orchestrator import Orchestrator


class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        knowledge_graph = KnowledgeGraph()
        input_data = InputData([1, 2, 3])
        orchestrator = Orchestrator(knowledge_graph)
        orchestrator.ingest_data(input_data)
        result = orchestrator.reason()
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()