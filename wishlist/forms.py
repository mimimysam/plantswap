from django.forms import ModelForm
from .models import Wish

class WishForm(ModelForm):
    class Meta:
        model = Wish
        fields = ('name', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'Enter wishlist item'})