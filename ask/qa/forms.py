from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'rows': '6',
        'placeholder': 'title',
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))

    def clean_title(self):
        title = self.cleaned_data['title']
        return title
    
    def clean_text(self):
        text = self.cleaned_data['text']
        return text
        
    def clean(self):
        pass
        
    def save(self, user):
        question = Question(**self.cleaned_data)
        question.author = user
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '3',
        'placeholder': 'answer!',
    }))
    question = forms.IntegerField(widget=forms.HiddenInput)
    
    def clean_text(self):
        text = self.cleaned_data['text']
        return text
        
    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            question = None
            raise forms.ValidationError(
                'Question does not exist',
                code='question_does_not_exist'
            )
        return question
        
    def clean(self):
        pass
    
    def save(self, user):
        answer = Answer(**self.cleaned_data)
        answer.author = user
        answer.save()
        return answer
        
class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def get_user(self):
        return self.cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def get_username(self):
        return self.cleaned_data['username']
        
    def get_password(self):
        return self.cleaned_data['password']
    