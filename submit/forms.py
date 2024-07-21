from django import forms
from submit.models import CodeSubmission

LANGUAGE_CHOICES = [
    ('py', 'Python'),
    ('c', 'C'),
    ('cpp', 'C++'),
]

class CodeSubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(choices = LANGUAGE_CHOICES)

    class Meta:
        Model = CodeSubmission
        fields = ['language', 'code', 'input_data']