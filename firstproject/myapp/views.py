from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user

from myapp.models import *


def check_login(func):
	def func_wrapper(*args, **kwargs):
		request = args[0]
		if not "username" in request.session:
			return redirect("login")
		return func(*args, **kwargs)
	return func_wrapper

@check_login
def index(request):
	if request.method == "POST":
		temperature = request.POST.get("temperature", 0)
		request.session["temperature"] = float(temperature)
	return render(request, "index.html", {
		"name": "YOU"
		})

@check_login
def authors(request):
	authors = Author.objects.all()
	return render(request, "authors.html", {
		"authors": authors
		})

@check_login
def author_edit(request, author_id):
	author = Author.objects.get(id=int(author_id))
	return render(request, "author_edit.html", {
		"author": author
		})

@check_login
def posts(request):
	posts = Post.objects.all()
	return render(request, "posts.html", {
		"posts": posts
		})

@check_login
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

@check_login
def post_delete(request, post_id):
	post = get_object_or_404(Post, id=int(post_id))
	post.delete()
	return redirect("posts")

@check_login
def delete_temperature(request):
	if "temperature" in request.session:
		del request.session["temperature"]
	return redirect("index")

def login(request):
	message = ""
	if request.method == "POST":
		is_user = authenticate(username=request.POST.get("username", ""),
			password=request.POST.get("password", ""))
		if is_user != None:
			get_authors = Author.objects.filter(user__username=request.POST["username"])
			if get_authors:
				request.session["username"] = get_authors[0].firstname
				return redirect("index")
			else:
				message = "Username not associated with author!"
		else:
			message = "Wrong username or password!"

	return render(request, "login.html", {
		"message": message
		})
		
@check_login
def logout(request):
	if "username" in request.session:
		del request.session["username"]
	return redirect("login")
