from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # context = {
    #     "variable1":"Hey there i am a variable",
    #     "variable2":"Akash is Great"
    # }
    # return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage.")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About page.")

def toolIntegrationServices(request):
    return render(request, 'toolIntegrationServices.html')
    # return HttpResponse("This is Tool Integration service page.")

def scriptingServices(request):
    return render(request, 'scriptingServices.html')
    # return HttpResponse("This is Tool Scripting service page.")

def websoftdevServices(request):
    return render(request, 'websoftdevServices.html')
    # return HttpResponse("This is Web and Software Development service page.")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contact = Contact(name = name, email = email, phone = phone, message = message, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
        
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page.")