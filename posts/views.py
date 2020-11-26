from django.shortcuts import render
from .forms import PostForm
from .models import Post


# Create your views here


def first(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/first.html', context)


def main(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return render('/thanks/')
    else:
        form = PostForm()
        return render('contact.html', {'form': form})


def new(request):

    form = PostForm()
    return render(request, 'posts/main.html', {'form': form})

