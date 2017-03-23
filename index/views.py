import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q

# Create your views here.
class IndexView(View):
    def get(self, request):

        return render(request, "index.html")



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