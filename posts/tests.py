from django.test import TestCase
from posts.models import Post, Products
from posts.forms import ProductCreateForm, PostCreateForm
from django.urls import reverse

# Create your tests here.
class PostTest(TestCase):

    def create_post(self, title="test", author="furgot", content="hello"):
        return Post.object.create(title=title, author=author,content=content)

    def test_post_creation(self):
        p = self.create_post()
        self.assertTrue(isinstance(p,Post))
        self.assertEqual(w.__unicode__(), w.title)