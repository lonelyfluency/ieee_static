from django import forms


class choiceForm(forms.Form):
    direction1 = forms.IntegerField()
    direction2 = forms.IntegerField()
    future_plan = forms.IntegerField()
