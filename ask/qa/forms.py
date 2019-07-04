from django import forms
from .models import Question, Answer

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
        
    def save(self):
        question = Question(**self.cleaned_data)
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
    
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer