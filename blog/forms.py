from django import forms
from . import models


# Class to create a form with the necessary fields to send to the database
# the information of a new article
class NewArticle(forms.ModelForm):
    class Meta:
        # Define the fields to be present and the model where they are
        # inherit from.
        model = models.Articles
        # Fields to include
        fields = ['title', 'body', 'slug', 'thumbnail']
