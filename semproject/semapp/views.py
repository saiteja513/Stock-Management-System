from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect
import matplotlib.pyplot as plt
import pandas as pd
from .forms import UserForm
from .models import User
import json
import os
from bsedata.bse import BSE


def index(request):
    return render(request, "index.html")

def search(request):
    return render(request,"search.html")

def stocks(request):
    req = request.POST
    stockname = req.get('stockName')
    print(stockname)
    return redirect("stocks/"+stockname)


def getStockDetails(request,stockName):
    b = BSE()
    dir_path = os.path.dirname(os.path.dirname(__file__))
    data = open(dir_path + "/static/stk.json").read()
    scripCodes = json.loads(data)

    stock = None
    history = None
    print(scripCodes.items())
    for code, name in scripCodes.items():
        if (stockName.lower() in name.lower()):
            try:
                stock = b.getQuote(code)
                history = b.getPeriodTrend(code, "1M")
                break
            except:
                continue
    if stock is None or history is None:
        return redirect('search')

    print(stock)
    print(history)
    return render(request,"stocks.html",{ "stock_data": history,"stockDetails":stock})


def register(request):
    form = UserForm()
    if request.method == "POST":
        formdata = UserForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg = "User Registered Successfully"
            return render(request, "register.html", {"uform": form, "msg": msg})
        else:
            msg = "Failed to Register User"
            return render(request, "register.html", {"uform": form, "msg": msg})
    return render(request, "register.html", {"uform": form})

def checkulogin(request):
    uname = request.POST.get("email" or "username")
    pwd = request.POST.get("password")

    flag = User.objects.filter((Q(email=uname) or Q(username=uname)) & Q(password=pwd))

    print(flag)

    if flag:
        u = User.objects.get(email=uname)
        print(u)
        request.session["id"] = u.id
        request.session["uname"] = u.name
        return redirect('search/')
    else:
        msg = "Login Failed"
        return render(request, "index.html", {"msg": msg})