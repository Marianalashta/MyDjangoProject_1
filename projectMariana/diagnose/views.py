from django.shortcuts import render
from django.views.generic.list import ListView
from diagnose.models import Post
from django.views.generic.detail import DetailView

class PostListView(ListView):
	model=Post
class PostDetailView(DetailView):
	
	model=Post
