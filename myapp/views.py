from django.shortcuts import render,redirect
from django.contrib.messages import constants as messages
from django.contrib import messages
from .models import Contact,Register

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

def register(request):
    return render (request, 'register.html')

def details_submit(request):
    if request.method=='POST':
        stname = request.POST['name']
        stemail = request.POST['email']
        stcontact = request.POST['phone']
        stprogram = request.POST['program']
        stnotes = request.POST['notes']
        stimage = request.FILES['image']
        insert = Register(name=stname,email=stemail,phone=stcontact,program=stprogram,notes=stnotes,photo=stimage)
        insert.save()
        messages.success(request, "Student Details Has Been Submited Successfully")
        return redirect('register_view')
    else:
        messages.error(request, 'Details invaild')
        return redirect('register')
    
def register_view(request):
    view_student = Register.objects.all()
    return render (request, 'register_view.html',{'student':view_student})
def delete(request,id):
    dataDelete = Register.objects.get(id=id)
    dataDelete.delete()
    messages.success(request, 'Data Has Been Deleted')
    return redirect('register_view')
def edit(request,id):
    edit_data = Register.objects.get(id=id)
    return render(request, 'edit.html',{'data':edit_data})
def edit_submit(request,id):
    if request.method=='POST':
        stname = request.POST['name']
        stemail = request.POST['email']
        stcontact = request.POST['phone']
        stprogram = request.POST['program']
        stnotes = request.POST['notes']
        update = Register.objects.get(id=id)
        update.name = stname
        update.email = stemail
        update.phone = stcontact
        update.program = stprogram
        update.notes = stnotes
        update.save()
        messages.success(request, "Data Updated Successfully")
        return redirect('register_view')
    else:
        messages.error(request, 'Details invaild')
        return redirect('register')