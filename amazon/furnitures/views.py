from django.shortcuts import render, redirect,get_object_or_404
from .models import Product
from .forms import ProductForm
from furnitures.models import Product

# Create your views here.
def home(request):
   prod = Product.objects.all()
   form = ProductForm()
   if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
            return redirect('home')
   return render(request, 'furnitures/home.html', {"prod":prod, "form":form})

def update_product(request,id):
    prod = get_object_or_404(Product,id=id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form =ProductForm(instance = prod)
    return render(request,'furnitures/update_product.html',{"form":form, "prod":prod})

def delete_product(request , id):
    prod = get_object_or_404(Product,id=id)
    prod.delete()
    return redirect('home')