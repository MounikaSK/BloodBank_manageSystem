from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from bloodapp.models import *
from django.contrib.auth.decorators import login_required
from .models import user

# Create your views here.
def home(request):
    return render(request,'home.html')

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def admin_login(request):
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        # user = authenticate(username=u, password=p)
        if u=="admin" and p=="admin":
                
                messages.success(request, "Logged in Successfully")
                return render(request,'admin_home.html')
        
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'admin_login.html')


def user_page(request):
    return render(request,'user.html')

def Login_User(request):
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        
        try:
            usr = user.objects.get(uname=u, pwd=p)
            request.session['user_id'] = usr.id  # Store user ID in session
            request.session['username'] = usr.uname  # Store username in session
            messages.success(request, "Logged in Successfully")
            return redirect('../user')  # Redirect to the user page
        except user.DoesNotExist:
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html')
    return render(request, 'login.html')







 

def signup(request):
    return render(request,'register.html')

def reg(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        dob = request.POST.get('dob')
        add = request.POST.get('add')
        bloodgroup = request.POST.get('bloodgroup')
        new_user = user(fname=fname, lname=lname, uname=uname, pwd=pwd, email=email, contact=contact, dob=dob, add=add, bloodgroup=bloodgroup)
        new_user.save()
        return render(request,'sucess.html')

def profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            usr = user.objects.get(id=user_id)
            return render(request, "profile.html", {'pro': usr})
        except user.DoesNotExist:
            return render(request, "profile.html", {'error': 'Profile does not exist.'})
    else:
        return redirect('login') 
        
        
        
def view_user(request):
    data = user.objects.all()
    return render(request,'view_user.html',{'d':data})


from django.urls import reverse
from django.shortcuts import redirect

def request_blood(request):
    if request.method == "POST":
        blood_group = request.POST['blood_group']
        quantity = request.POST['quantity']
        request_user_id = request.session.get('user_id')

        if request_user_id:
            try:
                request_user = user.objects.get(id=request_user_id)
                blood_request = BloodRequest(
                    user=request_user,
                    blood_group=blood_group,
                    quantity=quantity
                )
                blood_request.save()
                messages.success(request, "Blood request submitted successfully.")
                # confirmation_url = reverse('confirmation', kwargs={
                #     'username': request_user.uname,
                #     'blood_group': blood_group,
                #     'quantity': quantity
                # })
                # return redirect(confirmation_url)
            except user.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect('login')
        else:
            messages.error(request, "You need to log in to request blood.")
            return redirect('login')

    return render(request, 'request_blood.html')

def confirmation(request, username, blood_group, quantity):
    context = {
        'username': username,
        'blood_group': blood_group,
        'quantity': quantity,
    }
    return render(request, 'confirmation.html', context)
def all_order(request):
    data = BloodRequest.objects.all()
    return render(request, "order.html",{'data':data})
""
def admin_home(request):
    return render(request,"admin_home.html")




def donate_blood(request):
    if request.method == "POST":
        health_issues = request.POST.get('health_issues')
        blood_level = request.POST.get('blood_level')
        place= request.POST.get('place')
        blood_group = request.POST.get('blood_group')
        request_user_id = request.session.get('user_id')

        if request_user_id:
            try:
                request_user = user.objects.get(id=request_user_id)
                blood_donation = BloodDonation(
                    user=request_user,
                    health_issues=health_issues,
                    blood_level=blood_level,
                    place=place,
                    blood_group=blood_group
                )
                blood_donation.save()
                messages.success(request, "Blood donation recorded successfully.")
                return redirect('../donation_confirmation')
            except user.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect('login')
        else:
            messages.error(request, "You need to log in to donate blood.")
            return redirect('login')

    return render(request, 'donate_blood.html')

def donation_confirmation(request):
    return render(request, 'donation_confirmation.html')

def donator_blood(request):
    data = BloodDonation.objects.all()
    return render(request, "donator.html",{'data':data})