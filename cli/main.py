import argparse
from packages.core.types import KnowledgeGraph, InputData
from services.orchestrator import Orchestrator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    args = parser.parse_args()

    knowledge_graph = KnowledgeGraph()
    input_data = InputData([int(i) for i in args.input.split(',')])
    orchestrator = Orchestrator(knowledge_graph)

    orchestrator.ingest_data(input_data)
    result = orchestrator.reason()

    print(result)

if __name__ == '__main__':
    main()