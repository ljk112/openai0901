from django.shortcuts import render

import os
import openai
# Create your views here.
openai.api_key = os.getenv("OPENAI_API_KEY")


def go(request):
    return render(request,"index.html")
def go2(request):
    return render(request,"home.html")


# def gogo(request):
#     job = request.GET.get('job')
#     age = request.GET.get('age')
#     sex = request.GET.get('sex')
#     if (request.GET.get('etc')):
#         etc= "특이사항으로는 "+str(request.GET.get('etc'))

    
#     #prompt = f"너는 약사로써, 나에게 영양제를 추천해줘야 하는 역할이다. 내 직업은 {job}, 내 나이는 {age}, 내 성별은 {sex}이다. 나에게 약을 추천해달라. 대답은 한국어로 해라."
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role":"system",
#                 "content": "너는 훌륭한 약사이자, 의사이다. 너의 역할은 나에게 영양제를 추천해주는 것이다.",
#             },
#             {
#                 "role":"user",
#                 "content":f" 내 직업은 {job}, 내 나이는 {age}, 내 성별은 {sex} 이다.. 나에게 3가지의 영양제를 추천해달라.{etc}"
#             },
#         ],
#         max_tokens=1000,
#     )
#     res = response['choices'][0]["message"]["content"]
#     return render(request, "answer.html", {'res': res})

def gogo(request):
    sec1 = request.GET.get('sec1')
    sec2 = request.GET.get('sec2')
    sec3 = request.GET.get('sec3')
    sec4 = request.GET.get('sec4')
    sec5 = request.GET.get('sec5')
    sec6 = request.GET.get('sec6')
    sec7 = request.GET.get('sec7')
    sec8 = request.GET.get('sec8')
    sec9 = request.GET.get('sec9')
    sec10 = request.GET.get('sec10')
    sec11 = request.GET.get('sec11')
    sec12 = request.GET.get('sec12')
    sec13 = request.GET.get('sec13')
    sec14 = request.GET.get('sec14')
    sec15 = request.GET.get('sec15')
    sec16 = request.GET.get('sec16')
    sec17 = request.GET.get('sec17')
    sec18 = request.GET.get('sec18')
    sec19 = request.GET.get('sec19')
    sec20 = request.GET.get('sec20')
    sec21 = request.GET.get('sec21')
    sec22 = request.GET.get('sec22')
    sec23 = request.GET.get('sec23')
    sec24 = request.GET.get('sec24')
    sec25 = request.GET.get('sec25')
    sec26 = request.GET.get('sec26')
    sec27 = request.GET.get('sec27')
    sec28 = request.GET.get('sec28')
    sec29 = request.GET.get('sec29')
    sec30 = request.GET.get('sec30')
    sec31 = request.GET.get('sec31')
    sec32 = request.GET.get('sec32')
    sec33 = request.GET.get('sec33')
    sec34 = request.GET.get('sec34')
    sec35 = request.GET.get('sec35')
    sec36 = request.GET.get('sec36')
    sec37 = request.GET.get('sec37')
    sec38 = request.GET.get('sec38')
    sec39 = request.GET.get('sec39')
    sec40 = request.GET.get('sec40')


    
    #prompt = f"너는 약사로써, 나에게 영양제를 추천해줘야 하는 역할이다. 내 직업은 {job}, 내 나이는 {age}, 내 성별은 {sex}이다. 나에게 약을 추천해달라. 대답은 한국어로 해라."

    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                        "role": "system",
                        "content": "성격유형검사를 하려고 한다.(5점: 매우 동의 / 1점: 매우 비동의)\n1. 활동 : 자기 중심적 내향형(Self-Centered Introvert); IS, 상호작용 중심형 내향형(Interaction-Oriented Introvert) - II자기중심적 외향형(Self-Centered Extrovert) -ES, 상호작용 중심형 외향형(Interaction-Oriented Extrovert) - EI\n2. 판단 : 논리(Logical) -L, 감정(Emotional) -E, 직관(Intuitive) -I, 분석(Analytical) -A\n3. 성향1 : 계획적(Planned)- P, 적응적(Adaptive) -A, 미루기(Procrastinator) -P, 즉흥적(Spontaneous) -S\n4. 성향2 : 개방적(Openness),성실적,목표지향적(Conscientiousness), 이기적(Selfish), 협력적(Cooperative)\n\n성격검사 양식이다.\n1. 활동\n새로운 사람들과의 만남을 통해 에너지를 얻는 편인가요? \n혼자 있는 시간을 즐기는 편인가요? \n다른 사람들과의 대화보다는 개인적인 활동이 더 편안한 편인가요? \n사람들과의 대화에서 주로 듣는 쪽이 아닌 이야기하는 편인가요? \n친한 친구들과의 소규모 모임을 즐기는 편인가요? \n새로운 사람들과의 대화보다는 익숙한 사람들과 대화하는 편인가요? \n활동적인 사람들과 시간을 보내는 것을 선호하나요? \n혼자 있을 때 자신의 생각에 깊이 몰두하는 편인가요? \n친구들과의 대화가 주는 에너지보다는 혼자 있는 시간이 더 즐거운 편인가요? \n소수의 친한 친구들과 지낼 때 더 편안한 편인가요? \n2. 판단\n주로 감정보다 논리와 사실에 의존하여 결정을 내리는 편인가요? \n자신의 감정을 표현하는 것이 어려운 편인가요? \n직관적으로 느끼는 감정보다는 분석과 판단을 우선시하는 편인가요? \n논리적인 사고보다는 직관과 감정을 중요시하는 편인가요? \n감정적인 상황에서도 논리적인 판단을 유지하는 편인가요? \n문제 해결에 있어서 감정적인 영향을 최소화하고 논리적인 판단을 선호하는 편인가요? \n감정의 영향을 받지 않고 논리적으로 판단하는 편인가요? \n감정보다는 사실과 데이터를 기반으로 결정하는 편인가요? \n논리적인 사고와 분석을 통해 문제를 해결하려는 편인가요? \n타인의 감정보다는 논리적인 근거에 따라 판단하는 편인가요? \n3. 성향1\n계획을 세우고 일정을 따라가는 것을 좋아하는 편인가요? \n예상되는 상황을 고려하여 계획을 세우는 편인가요? \n예기치 않은 일에도 미리 준비해놓은 계획을 따르려는 편인가요? \n상황이 변해도 빠르게 적응하여 문제를 해결하려는 편인가요? \n융통성 있게 상황에 따라 대처하는 편인가요? \n계획이나 일정을 중시하는 편인가요? \n새로운 환경에 빠르게 적응하여 문제를 해결하려는 편인가요? \n계획을 변경해야 할 때 조직적으로 재조정하는 것을 선호하는 편인가요? \n계획을 세워놓고 따르는 것을 좋아하나요? \n새로운 상황에서도 융통성 있게 대처하는 편인가요? \n4. 성향2\n다양한 분야에 대한 흥미와 호기심을 가지고 있는 편인가요? \n다른 사람들과 협력하여 공동 목표를 달성하는 것을 중요하게 여기나요? \n협력과 조화를 중요하게 생각하며 타인의 의견을 존중하는 편인가요? \n다른 사람들과의 관계를 통해 더 큰 목표를 달성하려는 편인가요? \n다른 사람들의 요구와 필요를 배려하여 행동하는 편인가요? \n개인적인 이익보다는 공동체나 그룹의 이익을 중요하게 여기는 편인가요? \n타인과의 갈등을 회피하며 협력적인 방법으로 문제를 해결하려는 편인가요? \n협력을 통해 좋은 결과를 얻는 것을 중요하게 여기나요? \n다른 사람들과 함께 일하거나 활동하는 것을 즐기는 편인가요? \n타인과 협력하여 공동의 목표를 달성하는 것을 중요하게 여기나요? "
                        },
                        {
                        "role": "user",
                        "content": f"각각의 값이\n활동=[{sec1},{sec2},{sec3},{sec4},{sec5},{sec6},{sec7},{sec8},{sec9},{sec10}]\n판단=[{sec11},{sec12},{sec13},{sec14},{sec15},{sec16},{sec17},{sec18},{sec19},{sec20}]\n성향1=[{sec21},{sec22},{sec23},{sec24},{sec25},{sec26},{sec27},{sec28},{sec29},{sec30}]\n성향2=[{sec31},{sec32},{sec33},{sec34},{sec35},{sec36},{sec37},{sec38},{sec39},{sec40}]\n인 사람에 대해서\n1. 이 사람 성격에 대해서 500자 이하로 간단히 요약하여 제시하라.\n2. MBTI처럼 각 지표에 해당하는 문자로 성격에 대한 값을 조합하여 나타내라."
                        }
                    ],
                    temperature=0.1,
                    max_tokens=700,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                    )
    res = response['choices'][0]["message"]["content"]
    return render(request, "answer.html", {'res': res})
