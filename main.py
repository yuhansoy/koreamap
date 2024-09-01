from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import date, timedelta

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    today = date.today().strftime("%Y-%m-%d")
    return templates.TemplateResponse("index.html", {"request": request, "date": today, "label": "Today's Date"})

@app.get("/tomorrow", response_class=HTMLResponse)
async def read_tomorrow(request: Request):
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    return templates.TemplateResponse("index.html", {"request": request, "date": tomorrow, "label": "Tomorrow's Date"})

@app.get("/chart", response_class=HTMLResponse)
async def show_chart(request: Request):
    return templates.TemplateResponse("chart.html", {"request": request})

@app.get("/map", response_class=HTMLResponse)
async def show_map(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})