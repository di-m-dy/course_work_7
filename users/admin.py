from django.contrib import admin

from users.models import User
from habits.models import Habit, Report

admin.site.register(User)
admin.site.register(Habit)
admin.site.register(Report)
