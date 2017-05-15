from django.shortcuts import render, redirect
from models import Products
from django.contrib import messages

# Create your views here;.
def index(request):
	getall = Products.objects.all()
	context = {
		'everything': getall
	}
	return render(request, 'products.html', context)

def new(request):
	return render(request, 'new.html')

def create(request):
	if request.method == "POST":
		new_product = Products.objects.build_product(request.POST)
		if 'errors' in new_product:
			for error in new_product['errors']:
				messages.error(request, error)
			return redirect('products/new')
		else:
			return redirect('/products')

def show(request, id):
	all_products = Products.objects.get(id=id)
	context = {
	'product_info': all_products
	}
	return render(request, "show.html", context)

def edit(request, id):
	edit_product = Products.objects.get(id=id)
	context = {
	'edit_this_product': edit_product
	}
	return render(request, "edit.html", context)

def update(request,id):
	if request.method == "POST":
		update_this = Products.objects.get(id=id)
		update_this.name = request.POST['name']
		update_this.description = request.POST['description']
		update_this.price = request.POST['price']
		update_this.save()
		
		return redirect('/products')

def delete(request, id):
    Products.objects.get(id=id).delete()
    return redirect('/products')