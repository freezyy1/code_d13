from django.forms import ModelForm, Textarea, Select
from .models import Advert, Reply, Announcer, Category
from django.contrib.auth.models import User


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['adv_name', 'category', 'image', 'content', 'video', 'file', 'announcer']
        widgets = dict(category=Select(choices=Category.objects.all(), attrs={"class": "form-control"}),
                       content=Textarea(attrs={"class": "form-control"}),
                       announcer=Select(choices=Announcer.objects.all(), attrs={"class": "form-control"}))


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('user', 'advert', 'text')
        widgets = {
            "user": Select(choices=User.objects.all(), attrs={"class": "form-control"}),
            "advert": Select(choices=Advert.objects.all(), attrs={"class": "form-control"}),
            "text": Textarea(attrs={"class": "form-control"})
        }
