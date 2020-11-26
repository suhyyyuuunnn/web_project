from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    _type = forms.ChoiceField(
        widget=forms.RadioSelect,
        label="게시글 종류 ",
        choices=Post.POST_TYPE,
        required=True
    )

    class Meta:
        model = Post
        fields = ['title', '_type', 'content', 'image', 'file', 'link']
        labels = {
            'title': '제목',
            'content': '내용',
            'image': '게시글 사진',
            'file': '게시글 파일',
            'link': '게시글 링크'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }