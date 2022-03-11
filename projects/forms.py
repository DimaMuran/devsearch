from django.forms import ModelForm, fields
from .models import Project
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        for key,value in self.fields.items():
            value.widget.attrs.update({'class':'input'})
            