import json

import requests
from bs4 import BeautifulSoup
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class IndexView(View):
    def get(self, request):

        return render(request, "index.html")


def download_pre(request):
    print request.is_ajax()
    if request.is_ajax() and request.method == 'GET':  # basic Flask structure
        # url = request.GET.get('url', "")
        # raw = requests.get(url)  # make a request to the URL
        # soup = BeautifulSoup(raw.text, 'html.parser')  # get the HTML
        # links = soup.find(property="og:image")  # find meta with property=og:image
        # image = links.get('content')  # get its content
        ddd = 'https://scontent-lga3-1.cdninstagram.com/t51.2885-15/e15/11376191_377053725824200_1391635741_n.jpg?dl=1'
        image = '< div id = "results" style = "display: block;" > < div class ="success" > < a href="https://scontent-lga3-1.cdninstagram.com/t51.2885-15/s750x750/sh0.08/e35/17332897_1306212269488516_3762536345096945664_n.jpg?dl=1" class ="button button_green" target="_blank" > Download image < / a > < / div > < / div >'
        # image = '< div class ="success" > < a href=' + ddd +' class ="button button_green" target="_blank" > Download image < / a > < / div > < / div >'
        while image != '':
            res = {
                'success': True,
                'data': {'url': ddd}

            }
            return JsonResponse(res)
        else:
            res = {
                'success': False,
                'data': {'url': ""}

            }
            return JsonResponse(res)


def index(request):
	if request.method=='GET' : #basic Flask structure
		url= request.GET.get('name', "")
		raw=requests.get(url) #make a request to the URL
		soup=BeautifulSoup(raw.text,'html.parser') #get the HTML

		links= soup.find(property="og:image") #find meta with property=og:image
		image=links.get('content') #get its content
		while image!='':
			return '<img src="'+image+'"'+ 'align="center">' #insert content in img tag

	return render(request, 'index1.html')

def ajaxchannel(request):
    search = request.POST.get('search', "")
    plat_name = request.POST.get('site', "all")
    type_name = request.POST.get('classify', "")
    filter_info = ""

    serialized_filter_info = json.dumps(list(filter_info), cls=DjangoJSONEncoder)

    name_dict = {
        'success': True,
        'data': {'page': 1,
                 'total': 1,
                 'liveList': serialized_filter_info}

    }
    return JsonResponse(name_dict)