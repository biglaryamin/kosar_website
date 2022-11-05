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

    
    def __init__(self, *args, **kwargs):
        super(TextForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "عنوان متن"
        self.fields['pre_text'].label = "پیش متن"
        self.fields['text'].label = "متن اصلی"
        self.fields['post_text'].label = "پس از متن"