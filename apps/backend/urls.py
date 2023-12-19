
from django.urls import path

from .views.projects import ProjectListView, ProjectUpdateView, ProjectCreateView, ProjectDeleteView
from .views.views import index

urlpatterns = [
    path('', view=index, name='home'),
    path('projects/', view=ProjectListView.as_view(), name='project-list'),
    path('projects/create/', view=ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/update/', view=ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', view=ProjectDeleteView.as_view(), name='project-delete'),
]
