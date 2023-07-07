from django.test import TestCase
from datetime import date

from .models import Comment, Post, User


# Test blog comment Form model

class TestModels(TestCase):
    def setUp(self):
        self.comment = Comment(
            name="Tester",
            email="test@mail.com",
            message="Test message",
            created_on="2024-06-15",
            approved=False,
        )

    def test_comment_form(self):
        self.assertEqual(self.comment.name, "Tester")
        self.assertEqual(self.comment.email, "test@mail.com")
        self.assertEqual(self.comment.message, "Test message")
        self.assertEqual(self.comment.created_on, "2024-06-15")
        self.assertEqual(self.comment.approved, False)


class TestModels(TestCase):
    def setUp(self):
        self.post = Post(
            title="Test Title",
            excerpt=6,
            updated_on="2024-06-05",
            content="Test Content",
            created_on="2023-06-05",
        )

    def test_blog_post_model(self):
        self.assertEqual(self.post.title, "Test Title")
        self.assertEqual(self.post.excerpt, 6)
        self.assertEqual(self.post.updated_on, "2024-06-05")
        self.assertEqual(self.post.content, "Test Content")
        self.assertEqual(self.post.created_on, "2023-06-05")
