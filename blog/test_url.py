# Blog View Tests
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase, Client
from django.urls import reverse


# Test that the correct views are used for blog and the post details


class TestBlogViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.blog_url = reverse('blog')
        self.post_detail_url = reverse('post_detail')

    def test_blog_GET(self):
        response = self.client.get(self.blog_url)
        self.assertTemplateUsed(response, "blog/blog.html")
        self.assertEqual(response.status_code, 200)

    def test_post_detail_GET(self):
        response = self.client.get(self.post_detail_url)
        self.assertTemplateUsed(response, "blog/blog/post_detail.html")
        self.assertEqual(response.status_code, 200)