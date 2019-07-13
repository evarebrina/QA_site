from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from . import models
from .forms import AskForm, AnswerForm, SignupForm, LoginForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


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
        'user': request.user,
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
    page = paginator.get_page(page)
    return render(request, 'list.html', {
        'questions': page.object_list,
        'page': page,
        'user': request.user,
    })


def question(request, id, *args, **kwargs):
    try:
        question = models.Question.objects.get(pk=id)
    except models.Question.DoesNotExist:
        raise Http404("Question does not exist")
    answers = models.Answer.objects.filter(question=question)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AnswerForm(request.POST)
            # if user changed question id
            # form.question = id
            if form.is_valid():
                answer = form.save(request.user)
                url = question.get_absolute_url()
                return HttpResponseRedirect(url)
        return HttpResponseRedirect('/login?next=' + request.get_full_path())
    else:
        form = AnswerForm(initial={'question': question.id})
    return render(request, 'question.html', {
        'form': form,
        'question': question,
        'answers': answers,
        'user': request.user,
    })


def like(request, id, *args, **kwargs):
    print(str(request.body))
    print('123')
    try:
        question = models.Question.objects.filter(pk=id).get()
    except models.Question.DoesNotExist:
        raise Http404("Question does not exist")
    if request.user.is_authenticated:
        print('USER IS AUTHENTICATED')
        likes = question.likes
    if request.user in likes.all():
        likes.remove(request.user)
    else:
        likes.add(request.user)
    question.save()
    return HttpResponse(likes.count())


@login_required(login_url='/login/')   
def ask(request, *args, **kwargs):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AskForm(request.POST)
            if form.is_valid():
                question = form.save(request.user)
                url = question.get_absolute_url()
                return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect('/login', {
                'continue': '/ask'
            })
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form,
        'user': request.user,
    })


def signup(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.get_user())
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form,
        'user': request.user,
    })


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        
        form = LoginForm(request.POST)
        if form.is_valid():
            
            user = authenticate(username=form.get_username(), password=form.get_password())
            if user is not None:
                login(request, user)
                url = request.GET.get('next', '/')
                return HttpResponseRedirect(url)
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form,
        'user': request.user,
    })


def logout_view(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/')