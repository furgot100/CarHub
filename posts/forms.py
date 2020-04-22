from django import forms
from posts.models import Post, Products, Event

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'