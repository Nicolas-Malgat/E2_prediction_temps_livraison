from fastapi import FastAPI, Request, Form
from starlette.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from work.model_interaction import predict_delivery_time

favicon_path = 'favicon.ico'
templates = Jinja2Templates(directory="templates/")

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent / "static"),
    name="static",
)

@app.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)

@app.get("/")
def form_post(request: Request):
    result = "Soumettez le formulaire"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/")
def form_post(
    request: Request, 
    distance:        int = Form(...), 
    estimated_delay: int = Form(...), 
    price:           int = Form(...), 
    freight_value:   int = Form(...), 
    weight:          int = Form(...), 
    volume:          int = Form(...), 
    products:        list = Form(...), 
    day:             str = Form(...), 
    month:           str = Form(...)
):

    # ['distance', 'estimated_delay', 'price', 'freight_value', 'weight',
    #    'volume', 'ferramentas_jardim', 'utilidades_domesticas',
    #    'moveis_escritorio', 'Friday', 'Monday', 'August', 'December',
    #    'February', 'January', 'July', 'June', 'March', 'May', 'November']

    ref_products = ['ferramentas_jardim', 'utilidades_domesticas', 'moveis_escritorio']
    ref_days = ['Friday', 'Monday']
    ref_months = ['August', 'December', 'February', 'January', 'July', 'June', 'March', 'May', 'November']

    OHE = []
    OHE += [ 1 if ref in products   else 0 for ref in ref_products]
    OHE += [ 1 if ref == day        else 0 for ref in ref_days]
    OHE += [ 1 if ref == month      else 0 for ref in ref_months]
    form_data = [distance, estimated_delay, price, freight_value, weight, volume] + OHE

    result = predict_delivery_time(form_data)
    result = str(round(result, 1)) + ' jours avant livraison'
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})