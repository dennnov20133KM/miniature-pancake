from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="base.html", 
        context={"bots": "bots"}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
