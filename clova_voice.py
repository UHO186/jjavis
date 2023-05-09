# -*- coding: utf-8 -*-
# // 네이버 음성합성 Open API 예제
import os
import sys
import urllib.request
import requests
import urllib, openpyxl, time
import simsims as si

def clova(datas):
    client_id = "0y2d4anvaa"
    client_secret = "4ZLCFEGYvpoiaC0SJ49rfpEhz8a1vBaL8X95ojEH"
    encText = urllib.parse.quote(datas)
    data = "speaker=nsayuri&volume=1&speed=0&pitch=2&format=mp3&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        print("TTS mp3 저장")
        response_body = response.read()
        with open('TTS.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)

""" 
curl -i -X POST \
	-H "Content-Type:application/x-www-form-urlencoded" \
	-H "X-NCP-APIGW-API-KEY-ID:{애플리케이션 등록 시 발급받은 client id값}" \
	-H "X-NCP-APIGW-API-KEY:{애플리케이션 등록 시 발급받은 client secret값}" \
	-d 'speaker=nara&text=만나서 반갑습니다&volume=0&speed=0&pitch=0&format=mp3' \
 'https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts'

a = si.sims('안녕')
print(type(a))
encText = ""
def clova_tts():
    client_id = "0y2d4anvaa"
    client_secret = "4ZLCFEGYvpoiaC0SJ49rfpEhz8a1vBaL8X95ojEH"
    encText = urllib.parse.quote('뭐해')
    datas = "speaker=nara&volume=0&speed=0&pitch=0&format=mp3&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/voice-premium/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=datas.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        print("TTS mp3 저장")
        response_body = response.read()
        with open('1112.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)

clova_tts() 
"""


