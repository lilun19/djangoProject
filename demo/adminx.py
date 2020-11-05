import xadmin
from .models import Student
class ControlStudent(object):
    list_display=('student_id','name','age','score')
    search_filed=('name')

xadmin.site.register(Student,ControlStudent)