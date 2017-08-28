from django.contrib import admin

from myapp.models import *


class PostAdmin(admin.ModelAdmin):
	def short_content(self, obj):
		return obj.content[:50]

	def divisions(self, obj):
		if obj.likes >= 10:
			return "A"
		elif obj.likes >= 5:
			return "B"
		else:
			return "C"

	short_content.short_description = "Content"
	divisions.short_description = "Likes"
	list_display = ("title", "short_content", "visible", "divisions")
	search_fields = ("title", "content")
	list_filter = ("creationdate", "likes", "dislikes")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
