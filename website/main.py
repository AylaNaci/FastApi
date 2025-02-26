from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import datetime

app = FastAPI()
templates = Jinja2Templates(directory="static")

# http://192.168.1.130:8000/
@app.get("/")
async def read_root():
    return {"Ayla": "Naci"}

# http://192.168.1.130:8000/site
@app.get("/site", response_class=HTMLResponse)
async def read_site(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# http://localhost:8000/
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)