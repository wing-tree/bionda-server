import json

import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from bionda.settings import get_secret
from forecast.models import Forecast

BASE_URL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/'


# Create your views here.
@csrf_exempt
def get_forecast(request):
    base_date = request.GET.get('base_date', None)
    base_time = request.GET.get('base_time', None)
    nx = request.GET.get('nx', None)
    ny = request.GET.get('ny', None)

    if base_date is None or base_time is None:
        return HttpResponse("base_date and base_time must be provided", status=400)

    if nx is None or ny is None:
        return HttpResponse("nx and ny must be provided", status=400)

    try:
        nx = int(nx)
        ny = int(ny)
    except ValueError:
        return HttpResponse("nx and ny must be integers", status=400)

    forecast = Forecast.objects.filter(
        nx=nx,
        ny=ny,
        base_date=base_date,
        base_time=base_time
    ).first()

    if forecast:
        return JsonResponse(forecast.response)
    else:
        params = {
            'serviceKey': get_secret('serviceKey'),
            'numOfRows': 290,
            'pageNo': 1,
            'dataType': 'JSON',
            'base_date': base_date,
            'base_time': base_time,
            'nx': nx,
            'ny': ny
        }

        res = request_forecast(params) # jsondate.

        Forecast(
            base_date=base_date,
            base_time=base_time,
            nx=nx,
            ny=ny,
            response=res
        ).save()

        return JsonResponse(res, status=200)


def request_forecast(params):
    url = BASE_URL + "getVilageFcst"
    response = requests.get(url=url, params=params)
    response = json.loads(response.content)

    return response
