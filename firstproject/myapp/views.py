from django.shortcuts import render, redirect, get_object_or_404

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
	if int(post_id):
		post = get_object_or_404(Post, id=int(post_id))
	else:
		post = None
	message = ""

	if request.method == "POST":
		if int(post_id) == 0:
			# create new post
			post = Post(title=request.POST["title"], 
				content=request.POST["content"], 
				likes=int(request.POST["likes"]), 
				dislikes=int(request.POST["dislikes"]))
			message = "Create success"
			post.save()
		else:
			# update existing post
			post = get_object_or_404(Post, id=int(post_id))
			post.title = request.POST["title"]
			post.content = request.POST["content"]
			post.likes = int(request.POST["likes"])
			post.dislikes = int(request.POST["dislikes"])
			message = "Update success"
			post.save()

	
	return render(request, "post_edit.html", {
		"post": post,
		"message": message,
		})

def post_delete(request, post_id):
	post = get_object_or_404(Post, id=int(post_id))
	post.delete()
	return render(request, "posts.html", {
		"posts": Post.objects.all(),
		"message": "Post deleted"
		})
