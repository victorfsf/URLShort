from django import forms
from shortener.models import URLBase


class StoreURLForm(forms.ModelForm):
    link_attrs = {
        'placeholder': 'Paste your URL here',
        'class': 'form-control',
    }
    
    link = forms.URLField(widget=forms.Textarea(attrs=link_attrs))
    
    def clean(self):
        return self.cleaned_data
    
    class Meta:
        model = URLBase
        fields = ('link',)
