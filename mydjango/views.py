from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
	param = {'hello':'hi buddy','bye':'good bye'}
	return render(request,'index.html',param)

def ex1(request):
	s = '''<h2> navigation</h2> <a href="https://www.hubrootsolutions.com">hubrootsolutions</a><br>'''
	return HttpResponse(s)

def analyze(request):
	djtext =  request.GET.get('text','default')
	removepunc = request.GET.get('removepunc','off')
	fullcaps = request.GET.get('fullcaps','off')
	newlineremover = request.GET.get('newlineremover','off')
	print(removepunc)
	print(djtext)
	if removepunc == "on":
		puctuations ='''!@#$%^&*(><.,)'''
		analyzed = ""
		for char in djtext:
			if char not in puctuations:
				analyzed = analyzed + char
		params={'anali':analyzed}
		return render(request,"analyze.html",params)
	elif(fullcaps=="on"):
		analyzed=""
		for char in djtext:
			analyzed = analyzed + char.upper()
		params={'anali':analyzed}
		return render(request,"analyze.html",params)
	elif(newlineremover=="on"):
		analyzed=""
		for char in djtext:
			if char !="\n":
			 analyzed = analyzed + char
		params={'anali':analyzed}
		return render(request,"analyze.html",params)
	else:
		return HttpResponse("error")
	
	

# def removepunc(request):
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse("analyze<a href='/'>back<a>")

# def about(request):
#     return HttpResponse("about<a href='/'>back<a>")

# def blog(request):
#     return HttpResponse()
