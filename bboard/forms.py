from django import forms
from .models import Bb, Rubric


class BbForm(forms.ModelForm):

    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                    label='Рубрика', help_text='Обязательно введите рубрику',
                                    widget=forms.widgets.Select(attrs={'size':4}))
    class Meta:
        model = Bb
        fields=('title', 'content', 'price', 'rubric')
