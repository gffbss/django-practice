__author__ = 'geoffreyboss'

from django.forms import ModelForm
from hollywood.models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie