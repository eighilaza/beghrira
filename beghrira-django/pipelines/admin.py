from django.contrib import admin
from pipelines.models import Pipeline

class PipelineAdmin(admin.ModelAdmin):
    list_display = ( 'project_name', 'ihm_port', 'slave_port' )

admin.site.register(Pipeline, PipelineAdmin)
