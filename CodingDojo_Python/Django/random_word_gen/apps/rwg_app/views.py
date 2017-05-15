from django.shortcuts import render, redirect
import random, string
from django.db import models

def index(request):
	if 'num_attempts' not in request.session:
		request.session['num_attempts'] = 0
	return render(request, 'rwg_app/index.html')
# Create your views here.
def generate(request):
	if request.method == "POST":
		request.session['num_attempts'] += 1
		generated_word = ''.join(random.choice(string.letters[26:] + string.digits) for _ in range(14))
	request.session['generated_word'] = generated_word
	return redirect('/')


