from django.shortcuts import render
from .models import Projects_Done,skills
# Create your views here.
def home(request):
    projects = Projects_Done.objects.all()
    projects_ = Projects_Done.objects.all()
    skills_ = skills.objects.all()
    return render(request,'basic_info/base.html',{'projects':projects,'projects_':projects_,'skills_':skills_})
    