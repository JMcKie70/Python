from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
def index(request):
	
	return render(request, "ev_app/index.html")

def create(request):
	if request.method == "POST":
		validated_user = User.objects.validate_user(request.POST)

		if 'error' in validated_user:
			for validation_error in validated_user['error']:
				messages.error(request, validation_error)
			return redirect('/')
		if "the_user" in validated_user:
			messages.success(request, validated_user["the_user"].email)
			return redirect('/success')

def success(request):
	users = User.objects.all()
	context = {
		'users': users
	}
	return render(request, "ev_app/result.html", context)
