#!/usr/bin/env python3
from src.graph.workflow import TelecomWorkflow
from src.milvus.vector_store import MilvusVectorStore
def main():
    print("LangGraph + Milvus Telecom Agent")
    products = [
        {"id": "P001", "name": "Mobile Plan Pro", "category": "mobile", "price": 49.99, "rating": 4.5},
        {"id": "P002", "name": "Internet Fiber 100Mbps", "category": "internet", "price": 39.99, "rating": 4.7},
    ]
    
    customers = [
        {"id": "C001", "name": "John Doe", "category": "mobile", "budget": 60.0},
    ]
    
    workflow = TelecomWorkflow()
    for customer in customers:
        result = workflow.execute(customer, products)
        print(f"Recommendations for {customer['name']}: {result.get('recommendations', [])}")

if __name__ == "__main__":
    main()