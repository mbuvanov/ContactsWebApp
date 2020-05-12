from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Comment

def index(request):
	latest_articles_ls = Article.objects.order_by('-pub_date')[:5]

	return render(request, 'articles/list.html', {'latest_articles_ls': latest_articles_ls})

def detail (request, article_id):
	try:
		a = Article.objects.get( id = article_id)
	except:
		raise Http404("Статья не найдена!")

	return render(request, 'articles/detail.html', {'article': a})
