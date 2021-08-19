from django.shortcuts import render
from . models import Contact
from django.contrib import messages

# Create your views here.

def home(request):
    context = {'home':'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')
        contacts = Contact(name=name, email=email, subject=subject, msg=msg)
        messages.success(request, 'Your request has send.')
        contacts.save()
       
    return render(request, 'core/contact.html', {'contact':'active'})
