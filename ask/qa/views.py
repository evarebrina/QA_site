from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse
from . import models
from .forms import AskForm, AnswerForm

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
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        # if user changed question id
        #form.question = id
        if form.is_valid():
            answer = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={ 'question': question.id })
    return render(request, 'question.html', {
        'form': form,
        'question': question,
        'answers': answers,
    })
    
def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form,
    })