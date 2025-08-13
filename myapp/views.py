from django.shortcuts import render,redirect
from django.contrib.messages import constants as messages
from django.contrib import messages
from .models import Contact

# Create your views here.
def home (request):
    return render (request,'home.html')
def about (request):
    return render (request, 'about.html')
def program (request):
    return render (request, 'program.html')
def gallery (request):
    return render (request, 'gallery.html')
def contact (request):
    return render (request, 'contact.html')

def contact_submit(request):
    if request.method=='POST':
        myname = request.POST['name']
        myemail = request.POST['email']
        mysubject = request.POST['subject']
        mymessage = request.POST['message']
        insert = Contact(name=myname,email=myemail,subject=mysubject,message=mymessage)
        insert.save()
        messages.success(request, "Contact has been Save")
        
        return redirect('contact')
    else:
        messages.error(request, "Invalid Crediantial")
        return redirect('contact')
