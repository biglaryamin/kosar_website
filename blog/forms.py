
from django import forms
from .models import Comment
 
class CommentForm(forms.ModelForm):
    # content = forms.CharField(label ="", widget = forms.Textarea(
    # attrs ={
    #     'class':'form-control',
    #     'rows':4,
    #     'cols':50
    # }))
    class Meta:
        model = Comment
        exclude =("user",)