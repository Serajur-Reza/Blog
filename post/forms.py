from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('comment', )