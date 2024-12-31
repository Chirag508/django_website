from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import blog,contact,product
from .forms import productForm,userreggistarationform
from django.contrib import messages
from django.core.mail import send_mail
import datetime

# Create your views here.
def show_home_page(request):
    return render(request,'home.html') 

def show_blogs_page(request):
    blogs = blog.objects.all()
    context ={
        'blogs':blogs,
    }
    return render(request,'blog_page.html',context)

def show_blog_detail(request,blog_id):
    blogs = blog.objects.get(id = blog_id)
    print(blogs)
    return render(request, 'blog_details.html', {'blogs': blogs})

def show_about_us_page(request):
    return render(request,'about_us.html')

def show_contact_us_page(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # print(name,email,phone,message)
        contacts = contact(name =name,email =email,phone =phone,message =message)
        contacts.save()
        subject = f"New Contact Us Message from {name}"
        message_body = f"""

        Name: {name}
        Email: {email}
        Phone: {phone}

        time:{datetime.datetime.now()}
        Message:
        {message}
        """
        from_email = 'chiragpanchal143143@gmail.com'
        recipient_list = ['chiragpanchal143143@gmail.com']  
        send_mail(subject, message_body, from_email, recipient_list)
    return render(request,'contact_us.html')

def show_registartion_page(request):
    if request.method=='POST':
        form = userreggistarationform(request.POST)
        if form.is_valid():
            messages.success(request, 'User registration successfull...')
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = userreggistarationform()
    return render(request,'registration_page.html',{'form':form})

def show_login_page(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('product')
        else:
            return redirect('login')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def show_product_page(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        if request.method=='POST':
            products = product.objects.all()
            form = productForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('product')
        else:
            form = productForm()
            products = product.objects.all()
            return render(request,'product_form.html',{'form':form,'products':products})

def delete_product_data(request,id):
    del_product = product.objects.get(id = id)
    print(f"{del_product} deleting this")
    del_product.delete()
    return redirect('product')

def update_product_data(request,id):
    products = product.objects.all()
    upd_product = product.objects.get(id = id)
    form = productForm(instance=upd_product)
    if request.method=='POST':
        form = productForm(request.POST,instance=upd_product)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        return render(request,'product_form.html',{'products':products,'form':form})