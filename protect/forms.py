from django.forms import ModelForm, BooleanField
from django.contrib.auth.models import User

from main_app.models import Reply


class UserForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля.
    class Meta:
        model = User
        fields = '__all__'


class RepliesForm(ModelForm):
    check_box = BooleanField(label='Прочитано')

    class Meta:
        model = Reply
        fields = {'check_box'}
