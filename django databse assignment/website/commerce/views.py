from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import *
from django.contrib import messages
# Create your views here.
def home(requests):
    info = CompanyInformation.objects.all().first()
    products = Product.objects.all()

    data = {
        'info':info,
        'products':products
    }

    return render(requests, 'home.html', data)

def about(requests):
    info = CompanyInformation.objects.all().first()
    products = Product.objects.all()

    data = {
        'info':info,
        'products':products
    }  
    return render(requests, 'about.html',data)

def contacts(requests):
    info = CompanyInformation.objects.all().first()
    products = Product.objects.all()

    data = {
        'info':info,
        'products':products
    }
    return render(requests, 'contact.html')

def product(requests):
    info = CompanyInformation.objects.all().first()   
    product = Product.objects.all()

    data = {
        'info':info,
        'product':product
    }

    return render(requests, "All.html", data)

def toys(request):
    info = CompanyInformation.objects.all().first()   
    products = Product.objects.all()  

    data = {
        'info': info,
        'products': products  
    }

    return render(request, "toys.html", data) 

def clothes(requests):
    info = CompanyInformation.objects.all().first()   
    products = Product.objects.all()  

    data = {
        'info': info,
        'products': products  
    }

    return render(requests, "clothes.html", data)
def electronics(requests):
    info = CompanyInformation.objects.all().first()   
    products = Product.objects.all()  

    data = {
        'info': info,
        'products': products  
    }
    return render(requests, "electronics.html", data)

def accessories(requests):
    info = CompanyInformation.objects.all().first()   
    products = Product.objects.all()  

    data = {
        'info': info,
        'products': products  
    }

    return render(requests, "accessories.html", data)

def form_success(request):
    return render(request, 'form_success.html')

def submit_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        address = request.POST.get('address')
        message = request.POST.get('message')

        submission = FormSubmission(email=email, name=name, address=address, message=message)
        submission.save()

        return redirect(reverse('form_success'))
    else:
        return render(request, 'form_template.html')

def form_success(request):
    # Fetch the latest form submission for display
    latest_submission = FormSubmission.objects.last()

    context = {
        'latest_submission': latest_submission
    }
    return render(request, 'form_success.html', context)
