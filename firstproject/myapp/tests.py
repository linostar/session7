from django.test import TestCase, Client

from myapp.models import *


class TestMyApp(TestCase):

	client = Client()

	def setUp(self):
		new_author = Author(firstname="Raed", lastname="Sayeh", age=23)
		new_author.save()
		Post(title="First Post", content="blah blah blah",
			likes=0, dislikes=0, author=new_author).save()

	def tearDown(self):
		Post.objects.all().delete()
		Author.objects.all().delete()

	def test_author_name(self):
		get_author = Author.objects.filter(firstname="Raed").first()
		self.assertEqual(str(get_author), "Raed Sayeh")

	def test_post_title(self):
		get_post = Post.objects.filter(title="First Post").first()
		self.assertEqual(str(get_post), "First Post")

	def test_like_percentage_zero(self):
		get_post = Post.objects.filter(title="First Post").first()
		self.assertEqual(get_post.like_percentage(), 0)

	def test_like_percentage_66(self):
		get_post = Post.objects.filter(title="First Post").first()
		get_post.likes = 80
		get_post.dislikes = 40
		get_post.save()
		self.assertEqual(get_post.like_percentage(), 66.67)

	def test_enter_index_with_logging_in(self):
		response = self.client.get("/")
		self.assertEqual(response.url, "/login/")

	def test_enter_index_after_logging_in(self):
		self.session = self.client.session
		self.session["username"] = "raed"
		self.session.save()
		response = self.client.get("/")
		# self.assertEqual(response.status_code, 200)
		self.assertTrue(response.content.decode('utf-8').find("Enter Temperature") > -1)
