from django import forms
from news.models import dailyNews


class Newsform(forms.ModelForm):
    class Meta:
        model = dailyNews
        fields= "__all__"