from django.shortcuts import render
from pipelines.models import Pipeline

def index(request):
    pipelines_list = Pipeline.objects.all()
    template = 'pipelines/pipelines.html'
    context = { 'pipelines_list' : pipelines_list }
    return render(request, template, context)
