from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

def index(request):
	return render(request, 'lr_app/index.html')

def register(request):
	if request.method == 'POST':
		registered_user = User.objects.register_user(request.POST)
		
		if 'error' in registered_user:
			for validation_error in registered_user['error']:
				messages.error(request, validation_error)
			return redirect('/')

		if "the_user" in registered_user:
			messages.success(request, registered_user['the_user'].first_name)
			request.session['loggedin_user'] = registered_user['the_user'].id
			return redirect('/success')

def login(request):
	if request.method == 'POST':
		loggedin_user = User.objects.login_user(request.POST)

		if 'error' in loggedin_user:
			for validation_error in loggedin_user['error']:
				messages.error(request, validation_error)
			return redirect('/')

		if "the_user" in loggedin_user:
			request.session['loggedin_user'] = loggedin_user['the_user']
			messages.success(request, "Logged in succesfully")
			return redirect('/success')


def success(request):
	user = User.objects.get(id = request.session['loggedin_user'])
	context = {
		'user': user
	}

	return render(request, 'lr_app/success.html', context)

def logout(request):
	del request.session['loggedin_user']
	return redirect('/')