from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from qa.models import Question, Answer, User

admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)
