import os 
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .mixins import FieldsMixin,FormValidMixin,AuthorAccessMixin,SuperUserAccessMixin

from blog.models import Article
from presentation_app.models import ImageModel, TextModel
from .models import User
from .forms import ProfileForm
from presentation_app.forms import ImageForm, TextForm

from django.contrib import messages
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer


class ArticlelList(LoginRequiredMixin , ListView):
#    queryset=Article.objects.all()
    template_name='registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin , FormValidMixin , FieldsMixin , CreateView):
    model        =Article
    template_name="registration/article-create-update.html"


class ArticleUpdate(AuthorAccessMixin , FormValidMixin , FieldsMixin , UpdateView):
    model        =Article
    template_name="registration/article-create-update.html"


class ArticleDelete(SuperUserAccessMixin , DeleteView):
    model        =Article
    success_url  = reverse_lazy('account:home')
    template_name="registration/article_confirm_delete.html"


class Profile(LoginRequiredMixin ,UpdateView):
    model = User
#    fields = ['username','email','first_name','last_name','special_user','is_author']  do it in forms!
    template_name = "registration/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("account:profile")


    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile,self).get_form_kwargs()
        kwargs.update({
            'user':self.request.user
        })
        return kwargs


# api_views
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


def delete_old_image(wallpaper_name):
    the_image = ImageModel.objects.filter(name=wallpaper_name)
    the_image.delete()


def delete_old_text(text_name):
    the_text = TextModel.objects.filter(name=text_name)
    the_text.delete()


def edit_mainpage(request):
    img_form = ImageForm()
    txtform = TextForm()
    if request.method == 'POST':
        if "btn1" in request.POST:
            img_form = ImageForm(request.POST, request.FILES)

            if img_form.is_valid():
                img_obj = img_form.save(commit=False)
                img_obj.name = "wallpaper1"
                delete_old_image(img_obj.name)
                img_obj.save()
                messages.success(request, "File saved" )                
            else:
                img_form = ImageForm()
        ########################################################################
        elif "btn2" in request.POST:
            img_form = ImageForm(request.POST, request.FILES)

            if img_form.is_valid():
                img_obj = img_form.save(commit=False)
                img_obj.name = "wallpaper2"
                delete_old_image(img_obj.name)
                img_obj.save()                
            else:
                img_form = ImageForm()
        ########################################################################
        elif "btn3" in request.POST:
            img_form = ImageForm(request.POST, request.FILES)

            if img_form.is_valid():
                img_obj = img_form.save(commit=False)
                img_obj.name = "wallpaper3"
                delete_old_image(img_obj.name)
                img_obj.save()                
            else:
                img_form = ImageForm()
        ########################################################################
        elif "btn4" in request.POST:
            img_form = ImageForm(request.POST, request.FILES)

            if img_form.is_valid():
                img_obj = img_form.save(commit=False)
                img_obj.name = "wallpaper4"
                delete_old_image(img_obj.name)
                img_obj.save()                
            else:
                img_form = ImageForm()
        ########################################################################
        elif "text1" in request.POST:
            txt_form = TextForm(request.POST, request.FILES)

            if txt_form.is_valid():
                txt_obj = txt_form.save(commit=False)
                txt_obj.name = "text1"
                delete_old_text(txt_obj.name)
                txt_obj.save()                
            else:
                txt_form = TextForm()
        ########################################################################
        elif "text2" in request.POST:
            txt_form = TextForm(request.POST, request.FILES)

            if txt_form.is_valid():
                txt_obj = txt_form.save(commit=False)
                txt_obj.name = "text2"
                delete_old_text(txt_obj.name)
                txt_obj.save()                
            else:
                txt_form = TextForm()


    return render(request, "registration/edit_main-page.html", {"img_form":img_form, "TextForm":TextForm})