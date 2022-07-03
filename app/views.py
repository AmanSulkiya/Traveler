from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from .models import Customer, Tour, Cart, Booked, Train
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

class TourView(View):
    def get(self, request):
        tour = Tour.objects.all()
        return render(request, 'app/home.html',
    {'tour':tour})




class BookingDetailView(View):
    def get(self, request, pk):
        tour = Tour.objects.get(pk=pk)
        return render(request, 'app/bookingdetail.html', {'tour':tour})






def book_now(request):
   return render(request, 'app/booknow.html')

def login(request):
 return render(request, 'app/login.html')

def add_to_cart(request):
    user=request.user
    tour_id = request.GET.get('prod_id')
    tour = Tour.objects.get(id=tour_id)
    Cart(user=user, tour=tour).save()
    return redirect('/cart')




class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',
        {'form': form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congrarulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html',
        {'form': form})
        

def profile(request):
 return render(request, 'app/profile.html')

def mybookings(request):
    op = Booked.objects.filter(user=request.user)
    return render(request, 'app/mybookings.html', {'order_placed':op})

    return render(request, 'app/mybookings.html')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        return render(request,'app/addtocart.html',{'carts':cart})

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        #print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_tour = [p for p in Cart.objects.all() if p.user == user ]
        #print(cart_tour)
        if cart_tour:
            for p in cart_tour:
                tempamount = (p.quantity* p.tour.discounted_price)
                amount += tempamount
                totalamount = amount +shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount': amount})
        else:
            return render(request, 'app/emptycart.html')

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(tour=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save() 
        amount = 0.0
        shipping_amount = 70.0
        cart_tour = [p for p in Cart.objects.all() if p.user ==request.user]
        for p in cart_tour:
            tempamount = (p.quantity* p.tour.discounted_price)
            amount += tempamount
           

        data = {
                'quantity': c.quantity,
                'amount':amount,
                'totalamount':amount + shipping_amount
            }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(tour=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save() 
        amount = 0.0
        shipping_amount = 70.0
        cart_tour = [p for p in Cart.objects.all() if p.user ==request.user]
        for p in cart_tour:
            tempamount = (p.quantity* p.tour.discounted_price)
            amount += tempamount
            
        data = {
                'quantity': c.qunatity,
                'amount':amount,
                'totalamount':amount + shipping_amount
            }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(tour=prod_id) & Q(user=request.user))
        c.delete() 
        amount = 0.0
        shipping_amount = 70.0
        cart_tour = [p for p in Cart.objects.all() if p.user ==request.user]
        for p in cart_tour:
            tempamount = (p.quantity* p.tour.discounted_price)
            amount += tempamount
           

        data = {
                'amount':amount,
                'totalamount':amount + shipping_amount
            }
        return JsonResponse(data)




def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add})

def blog(request):
    return render(request, 'app/blog.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

def flight(request):
    return render(request, 'app/flight.html')

def train(request):
    return render(request, 'app/train.html')

def buses(request):
    return render(request, 'app/buses.html')


class TrainView(View):
    def get(self,request):
        data = Train.objects.all()
        return render(request, 'app/strain.html',{'data':data})
    

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request. POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
        return render(request, 'app/profile.html', {'form':form,
        'active':'btn-primary'})

def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    totalamount = 0.0
    tax_amount = 70.0
    cart_tour = [p for p in Cart.objects.all() if p.user == request.user]
    
    if cart_tour:
        for p in cart_tour: 
            tempamount = (p.quantity * p.tour.discounted_price)
            amount += tempamount
        totalamount = amount + tax_amount
    return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items}) 

def payment_done(request):
    user =request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        Booked(user=user, customer=customer, tour=c.tour, quantity=c.quantity).save()
        c.delete()
    return redirect("mybookings")


