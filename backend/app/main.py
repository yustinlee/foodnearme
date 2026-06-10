from fastapi import FastAPI
from app.routes import restaurants

app = FastAPI()
app.include_router(
    restaurants.router,
    prefix="/restaurants",
    tags=["restaurants"]
) # add a router tag incase of more routes in restaurants.py

@app.get("/")
def root():
    return {"message": "Food Near Me API"}
