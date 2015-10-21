from django.shortcuts import render
from pipelines.models import Pipeline, PipelineForm

def index(request):
    pipelines_list = Pipeline.objects.all()
    template = 'pipelines/index.html'
    context = { 'pipelines_list' : pipelines_list }
    return render(request, template, context)

def create(request):
    template = 'pipelines/create.html'
    form = PipelineForm(request.POST or None)
    context = { 'form': form }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    if request.method == 'POST':
        context = { 'thanks' : 'Thank you, your pipeline was instanciated' }
    return render(request, template, context)
