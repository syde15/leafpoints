from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from core.forms import UserForm
from core.models import Product
from core.models import Transaction
from datetime import date

def index(request):
    return HttpResponse(render(request, "core/index.html"))
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse("Bro... your account is disabled")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, "core/login.html")

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect('core/catalog.html')
        # else:
        #     print user.form_errors
    else:
        user_form = UserForm()
    return render(request, 'core/register.html', {'user_form': user_form, 'registered': registered})

def catalog(request):
    product_list = Product.objects.all()
    return render(request, 'core/catalog.html', {'products': product_list})

def leafs(request):
    transaction_list = Transaction.objects.all().filter(user_id=1)
    water_xdata= ["09-14", "10-14", "11-14", "12-14", "01-15", "02-15", "03-15", "04-15"]
    water_ydata = [150, 156, 225, 231, 180, 165, 145, 70]
    water_data = {
        'x': water_xdata, 'name1': 'Month', 'y1': water_ydata, 'name2': 'Liters Saved',
    }
    emission_xdata= ["09-14", "10-14", "11-14", "12-14", "01-15", "02-15", "03-15", "04-15"]
    emission_ydata = [10, 15, 22, 31, 18, 65, 45, 7]
    emission_data = {
        'x': emission_xdata, 'name1': 'Month', 'y1': emission_ydata, 'name2': 'CO2 Emissions Saved',
    }
    data = {
        'water_data': water_data,
        'emission_data': emission_data,
        'score': 75,
        'league': 2,
        'type': 5,
        'year': 2015,
        'plan': 6
    }  
    return render(request, 'core/leafs.html', data)

def shadowing(request):
    return render(request, 'core/shadowing.html')

def redeem(request):
    return render(request, 'core/redeem.html')