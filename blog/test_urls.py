# Test Booking URLS 
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from blog.views import (
    PostList,
    PostDetail,
    PostLike
)


# Test that all the correct urls are used when requested


class TestBlogUrls(SimpleTestCase):
    """
    This class is for testing the bookings app
    urls
    """

    def test_PostList_resolved(self):
        url = reverse("blog")
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_PostDetail_resolved(self):
        url = reverse("<slug:slug>")
        self.assertEquals(resolve(url).func.view_class, PostDetail)