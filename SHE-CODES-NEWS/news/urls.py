from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    #added for story search#
    path('searchStories/', views.searchStories, name='searchStories'),
    #end of added
    #added for filter my Stories
    path('myStories/', views.MyStoriesView.as_view(), name='myStories'),
    #end of added
    #added for comments
    path('comment/<int:pk>', views.AddCommentView.as_view(), name='addComment'),
    path('authorStories/<int:pk>', views.AuthorStoriesView.as_view(), name='authorStories' ),
    path('updateStories/<int:pk>', views.UpdateStory.as_view(), name='updateStory'),
]
