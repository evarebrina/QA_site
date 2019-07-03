from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.urls import reverse
from . import models

def test(request, *args, **kwargs):
    return HttpResponse('OK')
# Create your views here.

def index(request, *args, **kwargs):
    questions = models.Question.objects.new()
    limit = 10
    try:
        page = request.GET.get('page', 1)
    except:
        page = 1
    paginator = Paginator(questions, limit)
    paginator.baseurl = "/?page="
    page = paginator.get_page(page)
    return render(request, 'list.html', {
        'questions': page.object_list,
        'page': page,
    })
    
def popular(request, *args, **kwargs):
    questions = models.Question.objects.popular()
    limit = 10
    try:
        page = request.GET.get('page', 1)
    except:
        page = 1
    paginator = Paginator(questions, limit)
    paginator.baseurl = reverse('popular') + "?page="
    #paginator.baseurl = "/popular/?page="
    page = paginator.get_page(page)
    return render(request, 'list.html', {
        'questions': page.object_list,
        'page': page,
    })
    
def question(request, id, *args, **kwargs):
    try:
        question = models.Question.objects.get(pk=id)
    except models.Question.DoesNotExist:
        raise Http404("Question does not exist")
        #return HttpResponseNotFound()
    answers = models.Answer.objects.filter(question=question)
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
    })