from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import NewsStory
from .forms import StoryForm, CommentForm 
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser

#added for searching
def searchStories(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        stories = NewsStory.objects.filter(content__contains=searched)

        return render(request, 'news/searchStories.html', {'searched':searched, 'stories':stories})
    else:
        return render(request, 'news/searchStories.html', {})
#endofadded

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


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

#shows author stories
class AuthorStoriesView(generic.DetailView):
    template_name = 'news/authorStories.html'
    model = CustomUser
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_stories'] = NewsStory.objects.filter(author=self.object.id)
        return context

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentView(generic.CreateView):
    form_class = CommentForm
    template_name = 'news/createComment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form)

    def get_success_url(self) -> str:
        pk = self.kwargs.get("pk")
        return reverse_lazy('news:story', kwargs={'pk':pk})
        