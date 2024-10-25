from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

from django.http import JsonResponse

import time

import json
import requests

registerNamevalue = []
datavalue = []
unitvalue = []

def getdata():
    # 获取token
    iot_tk_url = "http://iot.lwbsq.com/api/getToken"

    iot_query = {
        "password": "vh240709szfc",
        "loginName": "vh240709szfc"
    }

    respon = requests.get(url=iot_tk_url, params=iot_query)

    data = respon.json()

    iot_token = data['data']['token']

    print()
    # print(iot_token)

    iot_search_url = "http://iot.lwbsq.com/api/data/getRealTimeData?"

    iot_search_header = {
        "Authorization": iot_token
    }

    iot_search_query = {
        "groupId": ""
    }

    respon1 = requests.get(url=iot_search_url, headers=iot_search_header, params=iot_search_query)

    data1 = respon1.json()

    ss = data1['data'][0]['dataItem']



    # range(0,2) 0、1
    for i in range(0, 2):
        registerNamevalue.append(ss[0]['registerItem'][i]['registerName'])
        datavalue.append(ss[0]['registerItem'][i]['data'])
        unitvalue.append(ss[0]['registerItem'][i]['unit'])

    for i in range(1, 9):
        registerNamevalue.append(ss[i]['registerItem'][0]['registerName'])
        datavalue.append(ss[i]['registerItem'][0]['data'])
        unitvalue.append(ss[i]['registerItem'][0]['unit'])

    # for i in range(0, 10):
    #     print(registerNamevalue[i])
    #     print(datavalue[i])
    #     print(unitvalue[i])


# Create your views here.
def index(request):
    registerNamevalue.clear()
    datavalue.clear()
    unitvalue.clear()
    getdata()
    # 风力、风速、风向、累计雨量、瞬时雨量、日雨量（昨日雨量）、空气湿度、CO2、光照、负氧离子
    data = {
        # 风力
        'wind_power_data':datavalue[0],
        'wind_power_unit':unitvalue[0],
        # 风速
        'wind_speed_data':datavalue[1],
        'wind_speed_unit':unitvalue[1],
        # 风向
        'wind_direction_data':datavalue[2],
        'wind_direction_unit':unitvalue[2],
        # 累计雨量
        'cumulative_rainfall_data':datavalue[3],
        'cumulative_rainfall_unit':unitvalue[3],
        # 瞬时雨量
        'instantaneous_rainfall_data':datavalue[4],
        'instantaneous_rainfall_unit':unitvalue[4],
        # 日雨量
        'daily_rainfall_data':datavalue[5],
        'daily_rainfall_unit':unitvalue[5],
        # 空气温度
        'air_humidity_data':datavalue[6],
        'air_humidity_unit':unitvalue[6],
        # CO2
        'CO2_data':datavalue[7],
        'CO2_unit':unitvalue[7],
        # 光照
        'light_data':datavalue[8],
        'light_unit':unitvalue[8],
        # 负氧离子
        'Negative_oxygen_ion_data':datavalue[9],
        'Negative_oxygen_ion_unit':unitvalue[9],
    }
    return JsonResponse(data)
