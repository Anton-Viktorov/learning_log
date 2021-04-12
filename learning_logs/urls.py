from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # homepage
    path('', views.index, name='index'),
    # Page with themes list
    path('topics/', views.topics, name='topics'),
    # Page with information on a specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding new theme
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
