from django.conf.urls import url

from myapp import views


urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^posts/$", views.posts, name="posts"),
	url(r"^post/(?P<post_id>\d+)/$", views.post_edit, name="post_edit"),
	url(r"^post/delete/(?P<post_id>\d+)/$", views.post_delete, name="post_delete"),
	url(r"^authors/$", views.authors, name="authors"),
	url(r"^author/(?P<author_id>\d+)/$", views.author_edit, name="author_edit"),
	url(r"^delete_temperature/$", views.delete_temperature, name="delete_temperature"),
	url(r"^login/$", views.login, name="login"),
	url(r"^logout/$", views.logout, name="logout"),
]
