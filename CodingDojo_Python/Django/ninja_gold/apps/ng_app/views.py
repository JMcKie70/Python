from django.shortcuts import render, redirect, HttpResponse
import datetime, random

def index(request):
	if 'gold_total' not in request.session:
		request.session["gold_total"] = 0
	if "message" not in request.session:
		request.session["message"] = []
	return render(request, 'ng_app/index.html')

def process(request):
	if "farm" in request.POST:
		earned_gold = random.randint(10, 20)
		location = "farm"
	
	if "cave" in request.POST:
		earned_gold = random.randint(5, 10)
		location = "cave"
	
	if "house" in request.POST:
		earned_gold = random.randint(2, 5)
		location = "house"
	
	if "casino" in request.POST:
		earned_gold = random.randint(-50, 50)
		location = "casino"

	if earned_gold < 0:
		new_message = 'Entered a casino and lost ' + str(-earned_gold) + ' gold coins... Ouch. ' + str(datetime.datetime.now())
		color = 'red'
	else:
		new_message = 'Earned ' + str(earned_gold) + " gold coins from the " +location+ "! " + str(datetime.datetime.now())
		color = 'green'

	request.session['gold_total'] += earned_gold
	
	

	request.session['message'].insert(0, {'new_message' : new_message, 'color' : color})
	print color
	print new_message
	
	return redirect('/')


    # request.session['activitylist'].insert(0, {"message" : 'You earned ' + str(earnings) + ' golds from the ' + str(request.POST['location']) + '! ' + str(datetime.datetime.now().strftime('%a %x %S')), "color" : "green" } )

    # return redirect('/')
    # message_dictionary = {'content': new_message, 'color': color}