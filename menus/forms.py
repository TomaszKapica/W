from django import forms
from .models import Item
from restaurants.models import Restaurant


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        print(user)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = Restaurant.objects.filter(owner=user)
