import unittest
from packages.utils.metrics import Metrics


class TestRuntime(unittest.TestCase):
    def test_metrics(self):
        metrics = Metrics()
        runtime = metrics.get_runtime()
        self.assertGreaterEqual(runtime, 0)

if __name__ == '__main__':
    unittest.main()