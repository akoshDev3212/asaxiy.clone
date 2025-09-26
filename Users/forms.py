from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Users.models import User



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Е-маил')
    first_name = forms.CharField(label='Имя', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    username = forms.CharField(label='Юзер', max_length=100)
    avatar = forms.ImageField(label='Аватар')
    country = forms.CharField(label='Страна', max_length=100)
    city = forms.CharField(label='Город', max_length=100)
    address = forms.CharField(label='Адрес', max_length=100)
    house = forms.CharField(label='Дом/Квартира', max_length=100)

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'username', 'email', 'country', 'city', 'address', 'house')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'email')