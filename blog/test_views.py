# Blog Views Tests
from django.test import TestCase, Client
from django.urls import reverse


class TestBlogViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.blog_url = reverse("blog")

    def test_PostList_GET(self):
        response = self.client.get(self.blog_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog.html")
