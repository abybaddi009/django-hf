from django import forms


class AskQuestionForm(forms.Form):
    passage = forms.CharField(label="Text Passage", required=True)
    question = forms.CharField(label="Question?")
