import unittest
from packages.core.types import KnowledgeGraph, InputData, ReasoningResult
from packages.core.engine import ReasoningEngine


class TestCore(unittest.TestCase):
    def test_reasoning_engine(self):
        knowledge_graph = KnowledgeGraph()
        input_data = InputData([1, 2, 3])
        engine = ReasoningEngine(knowledge_graph)
        engine.ingest_data(input_data)
        result = engine.reason()
        self.assertIsInstance(result, dict)

    def test_knowledge_graph(self):
        knowledge_graph = KnowledgeGraph()
        knowledge_graph.add('item1')
        knowledge_graph.add('item2')
        self.assertEqual(len(knowledge_graph.data), 2)

    def test_reasoning_result(self):
        result = {'a': 'b'}
        reasoning_result = ReasoningResult(result)
        self.assertEqual(reasoning_result.get_result(), result)

if __name__ == '__main__':
    unittest.main()