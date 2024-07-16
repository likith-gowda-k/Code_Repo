from .models import WatchesUploads
from django import forms

class UploadForm(forms.ModelForm):
    class Meta:
        model = WatchesUploads
        fields = ['name', 'description', 'price', 'image']