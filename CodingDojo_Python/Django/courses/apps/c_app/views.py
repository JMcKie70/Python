from django.shortcuts import render, HttpResponse, redirect
from .models import Course

def index(request):
	context= {
		"courses": Course.objects.all()
	}
	return render(request, 'c_app/index.html', context)

def add(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect("/")

def delete(request, id):
	context= {
		"del_course":Course.objects.get(id=id)
		#Course.objects.get(description)
	}
	
	return render(request, 'c_app/delete.html', context)

def action(request, id):
		Course.objects.get(id=id).delete()#delete course from database
		return redirect('/')

	
		
