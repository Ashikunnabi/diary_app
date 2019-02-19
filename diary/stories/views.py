from django.shortcuts import render, redirect
from .models import Story
from .forms import StoryForm

def index(request):
    stories = Story.objects.order_by('-date_posted')

    context = {'entries' : stories}

    return render(request, 'entries/index.html', context)

def add(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StoryForm()

    context = {'form' : form}

    return render(request, 'entries/add.html', context)