from typing import Dict
from logging import getLogger
from packages.core.engine import ReasoningEngine

logger = getLogger(__name__)

class RuntimeExecutor:
    def __init__(self, reasoning_engine: ReasoningEngine):
        self.reasoning_engine = reasoning_engine

    def execute(self) -> Dict[str, str]:
        logger.info('Runtime executor started')
        result = self.reasoning_engine.reason()
        logger.info(f'Runtime executor result: {result}')
        return result

    def ingest_data(self, input_data: object) -> None:
        logger.info(f'Ingesting data: {input_data}')
        self.reasoning_engine.ingest_data(input_data)
