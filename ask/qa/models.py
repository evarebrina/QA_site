from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Model):
    def new(self):
	    return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')
		
class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    addes_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    likes = models.ForeignKey(User, related_name='question_like_user', null=True, on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.pk

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.OneToOneField(Question, null=True, on_delete=models.SET_NULL)
    author = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
