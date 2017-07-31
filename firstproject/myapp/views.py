from django.shortcuts import render, redirect

from myapp.models import *


def index(request):
	return render(request, "index.html", {
		"name": "YOU"
		})

def authors(request):
	authors = Author.objects.all()
	return render(request, "authors.html", {
		"authors": authors
		})

def author_edit(request, author_id):
	author = Author.objects.get(id=int(author_id))
	return render(request, "author_edit.html", {
		"author": author
		})

def posts(request):
	posts = Post.objects.all()
	return render(request, "posts.html", {
		"posts": posts
		})

def post_edit(request, post_id):
	post = Post.objects.get(id=int(post_id))
	return render(request, "post_edit.html", {
		"post": post
		})
