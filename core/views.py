from django.shortcuts import render
import json

import requests
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


# Create your views here.
# Hi Or, i decided to pick a file form internet
# In this case, my picture form GitHub

@csrf_protect
def detect_face(request):
  
  subscription_key = 'a3cc922d0766458dba581f838eead5e9'
  headers = {'Ocp-Apim-Subscription-Key': subscription_key}
  params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'recognitionModel': 'recognition_03',
    'returnRecognitionModel':'true',
    'detectionModel': 'detection_01',
    'returnFaceId': 'true'
  }
  face_api = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect'
  url_image =  'https://avatars1.githubusercontent.com/u/12957575?s=400&u=838c65fc2550047243f94caf21e2c40614a5dd12&v=4'
  data = requests.post(face_api, params=params, headers=headers, json={"url": url_image})
  jsonData = data.json()
  dictData={}
  dict1={}
# Just to know we have everything on hands!
# nice to check:(Start) 
  for elementData in jsonData:
    for item in elementData:
      dictData[item]=elementData[item];
#      print(item);
#      print(dictData[item])
#      print("-----------------------------------")

# nice to check:(End)
  contextData = {'dictData': dictData }
  return render(request,'detectface.html', contextData)

