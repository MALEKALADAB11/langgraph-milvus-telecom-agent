from langgraph.graph import StateGraph, END
from typing import Dict, Any, List
from src.agents.product_analyzer import ProductAnalyzerAgent
from src.agents.recommendation_engine import RecommendationEngineAgent

class TelecomWorkflow:
    """LangGraph workflow orchestrating the two agents"""
    
    def __init__(self):
        self.product_analyzer = ProductAnalyzerAgent()
        self.recommendation_engine = RecommendationEngineAgent([], [])
        self.workflow = self._build_workflow()
    
    def _build_workflow(self):
        """Build the LangGraph workflow"""
        workflow = StateGraph()
        
        # Add nodes
        workflow.add_node("analyze_products", self._analyze_products_node)
        workflow.add_node("generate_recommendations", self._generate_recommendations_node)
        
        # Add edges
        workflow.add_edge("analyze_products", "generate_recommendations")
        workflow.add_edge("generate_recommendations", END)
        
        # Set entry point
        workflow.set_entry_point("analyze_products")
        
        return workflow.compile()
    
    def _analyze_products_node(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Node 1: Analyze products"""
        products = state.get("products", [])
        analyzed_products = []
        
        for product in products:
            analysis = self.product_analyzer.analyze(product)
            analyzed_products.append(analysis)
        
        state["analyzed_products"] = analyzed_products
        return state
    
    def _generate_recommendations_node(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Node 2: Generate recommendations"""
        customer = state.get("customer", {})
        products = state.get("analyzed_products", [])
        
        self.recommendation_engine.customer_data = [customer]
        self.recommendation_engine.product_data = products
        
        recommendations = self.recommendation_engine.generate_recommendations()
        
        state["recommendations"] = recommendations
        return state
    
    def execute(self, customer: Dict, products: List[Dict]) -> Dict[str, Any]:
        """Execute the workflow"""
        initial_state = {
            "customer": customer,
            "products": products,
            "analyzed_products": [],
            "recommendations": []
        }
        
        result = self.workflow.invoke(initial_state)
        return result