from fastapi import FastAPI
import uvicorn
from mylib.logic import recipe

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Recipe parser API. Call /recipe/?url=<recipe_url>"}

@app.get("/recipe/")
async def get_recipe(url: str):
    """Parse recipe"""
    return {"result": recipe(url)}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
