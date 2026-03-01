from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS configuration
origins = ["*"]  # Adjust this depending on the domains you want to allow
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products/")
async def read_products():
    logger.info("Fetching product list...")
    products = [
        {"id": 1, "name": "Product A", "price": 10.99},
        {"id": 2, "name": "Product B", "price": 12.99},
        {"id": 3, "name": "Product C", "price": 15.49},
    ]
    logger.info("Products fetched successfully.")
    return products

@app.get("/recommendations/{product_id}")
async def get_recommendations(product_id: int):
    logger.info(f"Fetching recommendations for product: {product_id}")
    recommendations = [
        {"id": 4, "name": "Recommended Product A", "price": 9.99},
        {"id": 5, "name": "Recommended Product B", "price": 11.99},
    ]
    logger.info("Recommendations fetched successfully.")
    return recommendations

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)