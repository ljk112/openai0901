from django.shortcuts import render

import os
import openai
# Create your views here.
openai.api_key = os.getenv("OPENAI_API_KEY")


def go(request):
    return render(request,"home.html")


def gogo(request):
    job = request.GET.get('job')
    age = request.GET.get('age')
    sex = request.GET.get('sex')
    prompt = f"너는 약사로써, 나에게 영양제를 추천해줘야 하는 역할이다. 내 직업은 {job}, 내 나이는 {age}, 내 성별은 {sex}이다. 나에게 약을 추천해달라. 대답은 한국어로 해라."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system",
                "content": "너는 훌륭한 약사이자, 의사이다. 너의 역할은 나에게 영양제를 추천해주는 것이다.",
            },
            {
                "role":"user",
                "content":f" 내 직업은 {job}, 내 나이는 {age}, 내 성별은 {sex} 이다.. 나에게 3가지의 영양제를 추천해달라."
            },
        ],
        max_tokens=1000,
    )
    res = response['choices'][0]["message"]["content"]
    return render(request, "answer.html", {'res': res})
