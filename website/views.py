from django.shortcuts import render
from django.views.generic import TemplateView
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def home(request):
    return render(request,'blog/index.html')


def absorption(request):
    C =''
    try:
        if request.method=="POST":
            absorption = request.POST.get('absorption')
            mydata = [[0,9],[3,6],[6,1.5],[9,1.5],[12,4]]
            df = pd.DataFrame(mydata,columns=['Percentage of TiB + 1.5Mg','Absorbed Energy (J)'])
            X = df['Percentage of TiB + 1.5Mg']
            y= df['Absorbed Energy (J)']
            poly = PolynomialFeatures(degree=4,include_bias=True)
            X = np.array(X).reshape(-1,1)
            y = np.array(y).reshape(-1,1)
            X_trans = poly.fit_transform(X)
            lr = LinearRegression()
            lr.fit(X_trans,y)
            value = np.array(absorption).reshape(-1,1)
            value = poly.fit_transform(value)
            C = lr.predict(value)
    except:
        C="INVALID INPUT"
    return render(request,'blog/absorption.html',{'C':C})



def elongation(request):
    C =''
    try:
        if request.method=="POST":
            elongation = request.POST.get('elongation')
            mydata = [[0,6.69],[3,4.93],[6,2.06],[9,0.7],[12,1.5]]
            df = pd.DataFrame(mydata,columns=['Percentage of TiB + 1.5Mg','Absorbed Energy (J)'])
            X = df['Percentage of TiB + 1.5Mg']
            y= df['Absorbed Energy (J)']
            poly = PolynomialFeatures(degree=4,include_bias=True)
            X = np.array(X).reshape(-1,1)
            y = np.array(y).reshape(-1,1)
            X_trans = poly.fit_transform(X)
            lr = LinearRegression()
            lr.fit(X_trans,y)
            value = np.array(elongation).reshape(-1,1)
            value = poly.fit_transform(value)
            C = lr.predict(value)
    except:
        C="INVALID INPUT"
    return render(request,'blog/elongation.html',{'C':C})
def tensile(request):
    C =''
    try:
        if request.method=="POST":
            tensile = request.POST.get('tensile')
            mydata =[[0,142.94],[3,179.17],[6,181.09],[9,190.46],[12,204.97]]
            df = pd.DataFrame(mydata,columns=['Percentage of TiB + 1.5Mg','Absorbed Energy (J)'])
            X = df['Percentage of TiB + 1.5Mg']
            y= df['Absorbed Energy (J)']
            poly = PolynomialFeatures(degree=4,include_bias=True)
            X = np.array(X).reshape(-1,1)
            y = np.array(y).reshape(-1,1)
            X_trans = poly.fit_transform(X)
            lr = LinearRegression()
            lr.fit(X_trans,y)
            value = np.array(tensile).reshape(-1,1)
            value = poly.fit_transform(value)
            C = lr.predict(value)
    except:
        C="INVALID INPUT"
    return render(request,'blog/tensile.html',{'C':C})
def vickers(request):
    C =''
    try:
        if request.method=="POST":
            vickers = request.POST.get('vickers')
            mydata =[[0,72],[3,74],[6,84],[9,86],[12,96]]
            df = pd.DataFrame(mydata,columns=['Percentage of TiB + 1.5Mg','Absorbed Energy (J)'])
            X = df['Percentage of TiB + 1.5Mg']
            y= df['Absorbed Energy (J)']
            poly = PolynomialFeatures(degree=4,include_bias=True)
            X = np.array(X).reshape(-1,1)
            y = np.array(y).reshape(-1,1)
            X_trans = poly.fit_transform(X)
            lr = LinearRegression()
            lr.fit(X_trans,y)
            value = np.array(vickers).reshape(-1,1)
            value = poly.fit_transform(value)
            C = lr.predict(value)
    except:
        C="INVALID INPUT"
    return render(request,'blog/vickers.html',{'C':C})
def wearloss(request):
    C =''
    try:
        if request.method=="POST":
            wearloss = request.POST.get('wearloss')
            mydata =[[0,0.001871],[3,0.001460],[6,0.000874],[9,0.000314],[12,0.000262]]
            df = pd.DataFrame(mydata,columns=['Percentage of TiB + 1.5Mg','Absorbed Energy (J)'])
            X = df['Percentage of TiB + 1.5Mg']
            y= df['Absorbed Energy (J)']
            poly = PolynomialFeatures(degree=4,include_bias=True)
            X = np.array(X).reshape(-1,1)
            y = np.array(y).reshape(-1,1)
            X_trans = poly.fit_transform(X)
            lr = LinearRegression()
            lr.fit(X_trans,y)
            value = np.array(wearloss).reshape(-1,1)
            value = poly.fit_transform(value)
            C = lr.predict(value)
    except:
        C="INVALID INPUT"
    return render(request,'blog/wearloss.html',{'C':C})
def youngs(request):
    C =''
    try:
        if request.method=="POST":
            youngs = request.POST.get('youngs')
            mydata =[[0,2902.435],[3,3679.325],[6,4774.951],[9,6584.659],[12,9970.27]]
            df = pd.DataFrame(mydata,columns=['Percentage of TiB + 1.5Mg','Absorbed Energy (J)'])
            X = df['Percentage of TiB + 1.5Mg']
            y= df['Absorbed Energy (J)']
            poly = PolynomialFeatures(degree=4,include_bias=True)
            X = np.array(X).reshape(-1,1)
            y = np.array(y).reshape(-1,1)
            X_trans = poly.fit_transform(X)
            lr = LinearRegression()
            lr.fit(X_trans,y)
            value = np.array(youngs).reshape(-1,1)
            value = poly.fit_transform(value)
            C = lr.predict(value)
    except:
        C="INVALID INPUT"
    return render(request,'blog/youngs.html',{'C':C})
