
from django.urls import path

from .views.projects import ProjectListView, ProjectUpdateView, ProjectCreateView, ProjectDeleteView, ProjectDetailView, ProjectFinishedList, ProjectOnGoingList, ProjectNotStartedList, StartProject, TerminateProject
from .views.service import ServiceListView, ServiceUpdateView, ServiceCreateView, ServiceDeleteView, ServiceDetailView
from .views.type import Entity_TypeListView, Entity_TypeUpdateView, Entity_TypeCreateView, Entity_TypeDeleteView, Entity_TypeDetailView
from .views.entities import enitities_list,create_new_entity, EntityListView, EntityUpdateView, EntityDeleteView, EntityDetailView
from .views.phase import phase_list, PhaseUpdateView, PhaseDeleteView, create_new_phase, phase_detail
from .views.tasks import task_list, TaskUpdateView, TaskDetailView, TaskDeleteView, create_new_task, startTask, terminateTask
from .views.function import FunctionCreateView, FunctionDeleteView, FunctionDetailView, FunctionListView, FunctionUpdateView
from .views.employee import EmployeeCreateView, EmployeeDeleteView, EmployeeDetailView, EmployeeListView, EmployeeUpdateView
from .views.views import index

urlpatterns = [
    path('', view=index, name='app-page'),
    #Porject routes
    path('projects/', view=ProjectListView.as_view(), name='project-list'),
    path('projects/ongoing/', view=ProjectOnGoingList, name='project-ongoing'),
    path('projects/finished/', view=ProjectFinishedList, name='project-finished'),
    path('projects/not-started/', view=ProjectNotStartedList, name='project-not-started'),
    path('projects/create/', view=ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/update/', view=ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', view=ProjectDeleteView.as_view(), name='project-delete'),
    path('projects/<int:pk>/detail/', view=ProjectDetailView.as_view(), name='project-detail'),
    path('projects/<int:pk>/start/', view=StartProject, name='start-project'),
    path('projects/<int:pk>/terminate/', view=TerminateProject, name='terminate-project'),
    #Phase routes
    path('phases/<int:project_id>/', view=phase_list, name='phase-list'),
    path('phases/create/<int:project_id>', view=create_new_phase, name='phase-create'),
    path('phases/<int:pk>/update/', view=PhaseUpdateView.as_view(), name='phase-update'),
    path('phases/<int:pk>/delete/', view=PhaseDeleteView.as_view(), name='phase-delete'),
    path('phases/<int:pk>/detail/', view=phase_detail, name='phase-detail'),
    #Task routes
    path('tasks/<int:phase_id>/', view=task_list, name='task-list'),
    path('tasks/create/<int:phase_id>', view=create_new_task, name='task-create'),
    path('tasks/<int:pk>/update/', view=TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', view=TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/<int:pk>/detail/', view=TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/start/', view=startTask, name='start-task'),
    path('tasks/<int:pk>/terminate/', view=terminateTask, name='terminate-task'),
    #Service routes
    path('services/', view=ServiceListView.as_view(), name='service-list'),
    path('services/create/', view=ServiceCreateView.as_view(), name='service-create'),
    path('services/<int:pk>/update/', view=ServiceUpdateView.as_view(), name='service-update'),
    path('services/<int:pk>/delete/', view=ServiceDeleteView.as_view(), name='service-delete'),
    path('services/<int:pk>/detail/', view=ServiceDetailView.as_view(), name='service-detail'),
    #entity_types routes
    path('types/', view=Entity_TypeListView.as_view(), name='entity-type-list'),
    path('types/create/', view=Entity_TypeCreateView.as_view(), name='entity-type-create'),
    path('types/<int:pk>/update/', view=Entity_TypeUpdateView.as_view(), name='entity-type-update'),
    path('types/<int:pk>/delete/', view=Entity_TypeDeleteView.as_view(), name='entity-type-delete'),
    path('types/<int:pk>/detail/', view=Entity_TypeDetailView.as_view(), name='entity-type-detail'),
    #entities routes
    path('entities/', view=EntityListView.as_view(), name='entity-list'),
    path('entities/service/<int:service_id>/', view=enitities_list, name='service-entities-list'),
    path('entities/service/<int:service_id>/create/', view=create_new_entity, name='entity-create'),
    path('entities/<int:pk>/update/', view=EntityUpdateView.as_view(), name='entity-update'),
    path('entities/<int:pk>/delete/', view=EntityDeleteView.as_view(), name='entity-delete'),
    path('entities/<int:pk>/detail/', view=EntityDetailView.as_view(), name='entity-detail'),
    #functions routes
    path('functions/', view=FunctionListView.as_view(), name='function-list'),
    path('functions/create/', view=FunctionCreateView.as_view(), name='function-create'),
    path('functions/<int:pk>/update/', view=FunctionUpdateView.as_view(), name='function-update'),
    path('functions/<int:pk>/delete/', view=FunctionDeleteView.as_view(), name='function-delete'),
    path('functions/<int:pk>/detail/', view=FunctionDetailView.as_view(), name='function-detail'),
    #employees routes
    path('employees/', view=EmployeeListView.as_view(), name='employee-list'),
    path('employees/create/', view=EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/<int:pk>/update/', view=EmployeeUpdateView.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', view=EmployeeDeleteView.as_view(), name='employee-delete'),
    path('employees/<int:pk>/detail/', view=EmployeeDetailView.as_view(), name='employee-detail'),
]
