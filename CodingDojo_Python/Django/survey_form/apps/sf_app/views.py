from django.shortcuts import render, HttpResponse, redirect
from django.db import models

def index(request):
	if 'num_submits' not in request.session:
		request.session['num_submits'] = 0
	return render(request, 'sf_app/index.html')

def process(request):
	if request.method == "POST":
		request.session['num_submits'] += 1
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
	return redirect('/result')

def result(request):
	return render(request, 'sf_app/result.html')

def back(request):
	return redirect('/')