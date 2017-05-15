from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.db.models import Count

def index(request):

	return render(request, 'db_app/index.html')

def register(request):
	if request.method == 'POST':
		registered_user = User.objects.register_user(request.POST)
		
		if 'error' in registered_user:
			for validation_error in registered_user['error']:
				messages.error(request, validation_error)

			return redirect('/')

		if "the_user" in registered_user:
			request.session['loggedin_user'] = registered_user['the_user'].id

			return redirect('/travels')

def login(request):
	if request.method == 'POST':
		loggedin_user = User.objects.login_user(request.POST)

		if 'error' in loggedin_user:
			for validation_error in loggedin_user['error']:
				messages.error(request, validation_error)
			return redirect('/')

		if "the_user" in loggedin_user:
			request.session['loggedin_user'] = loggedin_user['the_user']
			return redirect('/travels')


def travels(request):

	return render(request, 'db_app/travels.html')

def logout(request):

	del request.session['loggedin_user']
	return redirect('/main')


