from django.shortcuts import render
from .models import Identity, Experience, Project, Education


# Create your views here.
def index(request):
    template_name = 'index.html'
    identity = Identity.objects.all()
    experience = Experience.objects.all()
    project = Project.objects.all()
    education = Education.objects.all()
    
    context = { "identity": identity, "experience": experience, "project": project, "education": education }
#    return render(request, 'index.html', context)
    return render(request, template_name, context)

'''
def id_listview(request):
    template_name = 'index.html'
    queryset1 = Identity.objects.all()
    context = {
        "object_list1": queryset1
    }
    return render(request, template_name, context)
    
def res_listview(request):
    template_name = 'resume.html'
    queryset2 = Experience.objects.all()
    queryset2 = Education.objects.all()
    context = {
        "object_list2": queryset1, "object_list2": queryset1
    }
    return render(request, template_name, context)

def pro_listview(request):
    template_name = 'index.html'
    queryset = Project.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)
    
'''