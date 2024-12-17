from django.contrib import admin
from user.models import User, Student
from officestaff.models import FeesHistory,LibraryHistory

admin.site.register(User)
admin.site.register(Student)
admin.site.register(FeesHistory)
admin.site.register(LibraryHistory)

