from django.urls import path
from . import views
from .views import UserQuestionsListView

urlpatterns = [
    path('',views.home,name='stackoverflow-home'),
    path('detail/<int:id>',views.detail,name='stackoverflow-detail_page'),
    path('save-comment',views.save_comment,name='save-comment'),
    path('save-upvote',views.save_upvote,name='save-upvote'),
    path('save-downvote',views.save_downvote,name='save-downvote'),
    path('ask-question',views.ask_form,name='ask-question'),
    path('tag/<str:tag>',views.tag,name='tag'),
    path('profile/',views.TotalProfile,name='profile'),
    path('tags',views.tags,name='tags'),
    path('user/<str:username>', UserQuestionsListView.as_view(), name='user-qstns'),
    
]