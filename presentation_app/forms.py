from django.forms import ModelForm
from .models import ImageModel, TextModel


class ImageForm(ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'


class TextForm(ModelForm):
    class Meta:
        model = TextModel
        fields = '__all__'