from django.forms import ModelForm
from .models import Plant

class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ('name', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'Enter available plant'})