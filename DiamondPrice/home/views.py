from django.shortcuts import render
from django.http import HttpResponse
import requests
import pandas as pd
import joblib

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def predict(carat,cut,table,clarity,color,x,y,z):

    loaded = joblib.load('home/static/polynomialDiamond.joblib')
    data = [[carat,cut,table,clarity,color,x,y,z]]
    col = ['carat','cut','table','clarity','color','x','y','z']
    num = pd.DataFrame(data, columns=col)
    result = loaded.predict(num)

    return(result[0])

def get_results(request):
    if(request.method == 'POST'):
        carat = request.POST.get('carat')
        cut = int(request.POST.get('cut'))
        table = request.POST.get('table')
        clarity = int(request.POST.get('clarity'))
        color = int(request.POST.get('color'))
        x = request.POST.get('x')
        y = request.POST.get('y')
        z = request.POST.get('z')

        result = predict(carat, cut, table, clarity, color, x, y, z)
        return render(request, 'result.html', {'price':result})