from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from blog.models import Article
from presentation_app.models import ImageModel
from .mixins import FieldsMixin,FormValidMixin,AuthorAccessMixin,SuperUserAccessMixin
from .models import User
from django.urls import reverse_lazy
from .forms import ProfileForm

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer

from presentation_app.forms import ImageForm


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
    model         =User
#    fields       =['username','email','first_name','last_name','special_user','is_author']  do it in forms!
    template_name ="registration/profile.html"
    form_class    =ProfileForm
    success_url   =reverse_lazy("account:profile")


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


def edit_mainpage(request):
    if request.method == 'POST':
        if "btn1" in request.POST:
            img_form = ImageForm(request.POST, request.FILES)

            if img_form.is_valid():
                img_form.save(commit=False)
                img_form.name = "wallpaper1"
                img_form.save()
                return render(request, "registration/edit_main-page.html", {"img_form":img_form})

            else:
                img_form = ImageForm()
                return render(request, "registration/edit_main-page.html", {"img_form":img_form})
        ########################################################################
        elif "btn2" in request.POST:
            img_form = ImageForm(request.POST, request.FILES)
            if img_form.is_valid():
                img_form.save(commit=False)
                img_form.name = "wallpaper2"
                img_form.save()
                return render(request, "registration/edit_main-page.html", {"img_form":img_form})

            else:
                img_form = ImageForm()
                return render(request, "registration/edit_main-page.html", {"img_form":img_form})
        ########################################################################
        elif "btn3" in request.POST:
            img_form = ImageForm(request.POST, request.FILES)

            if img_form.is_valid():
                img_form.save(commit=False)
                img_form.name = "wallpaper3"
                img_form.save()                
                return render(request, "registration/edit_main-page.html", {"img_form":img_form})

            else:
                img_form = ImageForm()
                return render(request, "registration/edit_main-page.html", {"img_form":img_form})
        ########################################################################
        elif "btn4" in request.POST:
            img_form = ImageForm(request.POST, request.FILES)

            if img_form.is_valid():
                img_form.save(commit=False)
                img_form.name = "wallpaper4"
                img_form.save()    
                return render(request, "registration/edit_main-page.html", {"img_form":img_form})

            else:
                img_form = ImageForm()
                return render(request, "registration/edit_main-page.html", {"img_form":img_form})







# Is it useful?
def save_file(request):
    if request.method == 'POST':
        img_form = ImageForm(request.POST or None)
        if img_form.is_valid():
            img_form.save()

    return render(request, "registration/edit_main-page.html", {"img_form":img_form})