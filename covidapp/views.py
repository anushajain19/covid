from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "961ed9f88fmshe18e0e196c60bd5p1bb94djsn2175267e64dc",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def helloworldview(request):
	noofresults = int(response['results'])
	mylist = []
	for x in range(0,noofresults):
		mylist.append(response['response'][x]['country'])
	if request.method=="POST":
		selectedcountry = request.POST['selectedcountry']
		noofresults = int(response['results'])
		for x in range(0,noofresults):
			if selectedcountry==response['response'][x]['country']:
				new = response['response'][x]['cases']['new']
				active = response['response'][x]['cases']['active']
				critical = response['response'][x]['cases']['critical']
				recovered = response['response'][x]['cases']['recovered']
				total = response['response'][x]['cases']['total']
				deaths = total - active - recovered
		context = {'selectedcountry' : selectedcountry, 'mylist' : mylist,'total': total,'new': new,'active' : active,'critical' : critical,'recovered' : recovered,'deaths' : deaths}
		return render(request,'helloworld.html',context)

	context = {'mylist': mylist}
	return render(request,'helloworld.html',context)
