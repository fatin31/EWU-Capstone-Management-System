from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import Student
from .models import Faculty
from .models import ProposedTopic
from .models import MeetingTable
from .models import GradeTable
from .models import Ad_panel


admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(ProposedTopic)
admin.site.register(MeetingTable)
admin.site.register(GradeTable)
admin.site.register(Ad_panel)
