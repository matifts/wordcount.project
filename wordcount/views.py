from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request, 'home.html')


def aboutpage(request):
	return render(request, 'about.html')

def count(request):
	fulltext = request.GET['fulltext']
	worldlist = fulltext.split()
	worddictionary = {}
	for word in worldlist:
		if word in worddictionary:
			#increase
			worddictionary[word] += 1
		else:
			#add to the dictionary

			worddictionary[word] = 1

	return render(request, 'count.html', {'fulltext': fulltext, 'count': len(worldlist), 'worddictionary':worddictionary.items()})

# def eggs(request):
# 	return HttpResponse('<h1>eggs are great!</h1>')