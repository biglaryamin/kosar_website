from django.shortcuts import render, get_object_or_404 , get_list_or_404
from .models import Article,Category
from account.models import User
from django.views.generic import ListView
from .forms import CommentForm
from django.views.generic.edit import CreateView


#api
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArticleSerializer


#404 view
def custom_page_not_found_view(request, exception):
    return render(request, "blog/404.html",{})


class ArticleList(ListView):
	template_name="blog/blog.html"
	queryset     	   =Article.objects.published()
	paginate_by  	   =3

	def get_context_data(self,**kwargs):
		context = super(ArticleList,self).get_context_data(**kwargs)
		context['last_three_articles'] = Article.objects.published().order_by('-publish')[0:3]
		context['cats'] = Category.objects.all()
		return context



def show_article_detail(request , slug):
	if request.method == 'POST':
		MyCommentForm=CommentForm(request.POST or None)
		if MyCommentForm.is_valid():
			mc=MyCommentForm.save(commit=False)	
			mc.article=get_object_or_404(Article.objects.all() , slug=slug)
			mc.save()
		else:
			MyCommentForm=CommentForm(request.POST or None)

	context={
		"article":get_object_or_404(Article.objects.published() , slug=slug),
		"cats":Category.objects.all(),
	}
	return render(request , "blog/blog-details.html" , context)



'''
def category(request, slug ,page=1):
	category     =get_object_or_404(Category, slug=slug ,status=True)
	articles_list=category.articles.published()
	paginator    = Paginator(articles_list, 3) # Show 3 contacts per
	articles     = paginator.get_page(page)
	context={
		"category":category,
		"articles":articles,
	}
	return render(request,"blog/category.html",context)'''


class CategoryList(ListView):
	paginate_by = 3
	template_name='blog/category-list.html'

	def get_queryset(self):
		global category
		slug=self.kwargs.get('slug')
		category=get_object_or_404(Category.objects.active() , slug=slug)
		return category.articles.published()

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['category']=category
		return context


class AuthorList(ListView):
	paginate_by = 3
	template_name='blog/author_list.html'

	def get_queryset(self):
		global author
		username=self.kwargs.get('username')
		author=get_object_or_404(User, username=username)
		return author.articles.published()

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['author']=author
		return context


def show_contact_page(request):
	return render(request, "blog/contact.html" )


def show_base_page(request):
	return render(request, "blog/base.html" )


def search(request):
	found_articles = Article.objects.none()
	if request.method == "POST":
		input_word=request.POST.get("input_search")
		found_articles = Article.objects.filter(title__contains = input_word)

	if found_articles:
		return render(request , "blog/search_articles.html" , {'object_list':found_articles})
	return render(request , "blog/search_not_found.html")


#api_views

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-created')
    serializer_class = ArticleSerializer
    # permission_classes = [permissions.IsAuthenticated]



def test_ajax(request):
	return render(request, "blog/list_ajax.html")
