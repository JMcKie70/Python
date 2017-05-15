from django.shortcuts import render, HttpResponse

def index(request):
	context = {
		'message' : "No Ninjas Here!"
	}
	return render(request, "dn_app/index.html", context)

def four_ninjas(request):
	context = {
		'show' : 'true'
	}
	return render(request, "dn_app/index.html", context)

def colored_ninja(request, id):
	context = {
		'color' : id
	}
	return render(request, 'dn_app/colored_ninja.html', context)
