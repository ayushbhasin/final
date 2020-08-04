from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Meetups)
admin.site.register(MeetupTypes)
admin.site.register(SubjectTypes)
admin.site.register(Buildings)
