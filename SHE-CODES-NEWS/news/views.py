from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm 
from django.shortcuts import render

#added for searching
def searchStories(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        stories = NewsStory.objects.filter(content__contains=searched)

        return render(request, 'news/searchStories.html', {'searched':searched, 'stories':stories})
    else:
        return render(request, 'news/searchStories.html', {})

#endofadded#

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()
        #context_object_name = "all_stories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        # first 5 stories published
        context['old_stories'] = NewsStory.objects.all().order_by('pub_date')[:4]
        return context

#shows all of my stories
class MyStoriesView(generic.ListView):
    template_name = 'news/myStories.html'

    def get_queryset(self):
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.request.user)
        return context

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
