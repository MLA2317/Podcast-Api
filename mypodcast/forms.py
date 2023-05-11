from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ['author', 'episode']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'comment_input',
            'id': 'name',
            'cols': 200,
            'rows': 5,
            'placeholder': 'name'

        })
        self.fields['text'].widget.attrs.update({
            'class': 'form-control',
            'id': 'message',
            'cols': 200,
            'rows': 5,
            'placeholder': 'message'
        })

