# Product Analyzer Agent
# This agent analyzes products in the telecom retail sector

from typing import Any, Dict

class ProductAnalyzerAgent:
    """Agent responsible for analyzing telecom products"""
    
    def __init__(self):
        self.name = "Product Analyzer"
        self.description = "Analyzes telecom products and their features"
    
    def analyze(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze product data and extract relevant features
        """
        analysis = {
            "product_id": product_data.get("id"),
            "name": product_data.get("name"),
            "category": product_data.get("category"),
            "features": product_data.get("features", []),
            "price": product_data.get("price"),
            "rating": product_data.get("rating")
        }
        return analysis