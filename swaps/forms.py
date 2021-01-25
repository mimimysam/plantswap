from django.forms import ModelForm
from myplants.models import Plant

class SearchForm(ModelForm):
    class Meta:
        model = Plant
        fields = ('name', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'Search for a plant...'})