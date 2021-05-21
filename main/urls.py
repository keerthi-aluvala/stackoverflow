from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='stackoverflow-home'),
    path('detail/<int:id>',views.detail,name='stackoverflow-detail_page'),
    path('save-comment',views.save_comment,name='save-comment'),
    path('save-upvote',views.save_upvote,name='save-upvote'),

]