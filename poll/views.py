from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


# 查选所有问题
@csrf_exempt
def index(request):
    question_list = Question.objects.all()  # 查询所有的问题
    datas = {}  # 定义存放问题标题内容的字典
    response_data = {}  # 定义存放返回信息的字典
    if question_list:
        for question in question_list:
            datas[question.id] = question.question_text
            response_data['status'] = '200'
            response_data['message'] = 'success'
            response_data['data'] = datas
            result = json.dumps(response_data)  # 将字段转换成json字符串
        return HttpResponse(result)
    else:
        response_data['status'] = '10021'
        response_data['message'] = 'null'
        response_data['data'] = datas
        result = json.dumps(response_data)
    return HttpResponse(result)


# 查看某个问题的选项
@csrf_exempt
def detail(request, question_id):
    choices = Choice.objects.filter(question_id=question_id)  # 通过问题id来查询某个问题的选项
    datas = {}
    response_data = {}
    if choices:
        for choice in choices:
            datas[choice.id] = choice.choice_text
            response_data['status'] = '200'
            response_data['message'] = 'success'
            response_data['data'] = datas
            result = json.dumps(response_data)
        return HttpResponse(result)
    else:
        response_data['status'] = '10021'
        response_data['message'] = 'null'
        response_data['data'] = datas
        result = json.dumps(response_data)
    return HttpResponse(result)


# 查看投票结果
@csrf_exempt
def results(request, question_id):
    results = Choice.objects.filter(question_id=question_id)
    datas = {}
    response_data = {}
    if results:
        for r in results:
            datas[r.choice_text] = r.votes  # 把某个选项的投票数量取出赋给字典
            response_data['status'] = '200'
            response_data['message'] = 'success'
            response_data['data'] = datas
            result = json.dumps(response_data)
        return HttpResponse(result)
    else:
        response_data['status'] = '10021'
        response_data['message'] = 'null'
        response_data['data'] = datas
        result = json.dumps(response_data)
    return HttpResponse(result)


# 投票
@csrf_exempt
def votes(request, question_id, index):
    p = get_object_or_404(Question, pk=question_id)  # 通过关键字问题id来取查询问题对象，如果没有该问题，就返回404
    results = Choice.objects.filter(question_id=question_id)
    # choice_id = request.POST.get('choice', '')
    response_data = {}
    if not results:
        response_data['status'] = '10021'
        response_data['message'] = 'null'
        result = json.dumps(response_data)
        return HttpResponse(result)
    else:
        choice_id = results[index].id
    try:
        selected_choice = p.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        response_data['status'] = '10022'
        response_data['message'] = 'The problem is not the choice id'
        result = json.dumps(response_data)
        return HttpResponse(result)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        response_data['status'] = '200'
        response_data['message'] = 'success'
        result = json.dumps(response_data)
    return HttpResponse(result)


# 投票
@csrf_exempt
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)  # 通过关键字问题id来取查询问题对象，如果没有该问题，就返回404
    # 兼容post和get请求
    if request.method == 'POST':
        choice_id = request.POST.get('choice', '')
    else:
        choice_id = request.GET.get('choice', '')
    print(request.POST)
    print(choice_id)
    # return HttpResponse(choice_id)
    response_data = {}
    if choice_id == '':
        response_data['status'] = '10021'
        response_data['message'] = 'null'
        result = json.dumps(response_data)
        return HttpResponse(result)
    try:
        # selected_choice = Choice.objects.get(pk=choice_id)
        selected_choice = p.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        response_data['status'] = '10022'
        response_data['message'] = 'The problem is not the choice id'
        result = json.dumps(response_data)
        return HttpResponse(result)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        response_data['status'] = '200'
        response_data['message'] = 'success'
        result = json.dumps(response_data)
    return HttpResponse(result)
