from django.shortcuts import render
from pipelines.models import Pipeline, PipelineForm

def index(request):
    pipelines_list = Pipeline.objects.all()
    template = 'pipelines/pipelines.html'

    form = PipelineForm(request.POST or None)

    context = { 'pipelines_list' : pipelines_list, 'form': form }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = { 'pipelines_list' : pipelines_list, 'form': 'Thanks you' }

    if request.method == 'POST':
        print request

    return render(request, template, context)

"""class PipelineView(PieplineForm):
    template = 'pipelines/pipelines.html'
    form_class = PipelineForm
    success_url = '/'
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        return super(PipelineView, self).form_valid(form)
"""
