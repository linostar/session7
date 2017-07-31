from django.conf.urls import url

from myapp import views


urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^posts/$", views.posts, name="posts"),
	url(r"^post/(?P<post_id>\d+)/$", views.post_edit, name="post_edit"),
	url(r"^authors/$", views.authors, name="authors"),
	url(r"^author/(?P<author_id>\d+)/$", views.author_edit, name="author_edit"),
]
