from django.urls import path
from hello.views import *
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", home, name="home"),
    path("hello/<name>", hello_there, name="hello_there"),
    path("home/zozo_home",  zozo_home, name="zozo_home" ),

# Users
    path('users',                    UserView.UserListView,   name='all'),
    path('user/<int:id>/detail',     UserView.UserDetailView, name='user_detail'),
    path('user/create/',             UserView.UserCreateView, name='user_create'),
    path('user/<int:id>/update/',    UserView.UserUpdateView, name='user_update'),
    path('user/<int:id>/delete/',    UserView.UserDeleteView, name='user_delete'),

# #Tickets
#     path('tickets',                  TicketListView.as_view(),   name='all'),
#     path('tickets/<int:pk>/detail',  TicketDetailView.as_view(), name='ticket_detail'),
#     path('tickets/create/',          TicketCreateView.as_view(), name='ticket_create'),
#     path('tickets/<int:pk>/update/', TicketUpdateView.as_view(), name='ticket_update'),
#     path('tickets/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),

# #Attachment
#     path('attachment',                  AttachmentListView.as_view(),   name='all'),
#     path('attachment/<int:pk>/detail',  AttachmentDetailView.as_view(), name='attachment_detail'),
#     path('attachment/create/',          AttachmentCreateView.as_view(), name='attachment_create'),
#     path('attachment/<int:pk>/update/', AttachmentUpdateView.as_view(), name='attachment_update'),
#     path('attachment/<int:pk>/delete/', AttachmentDeleteView.as_view(), name='attachment_delete'),

# #Department
#     path('department',                  DepartmentListView.as_view(),   name='all'),
#     path('department/<int:pk>/detail',  DepartmentDetailView.as_view(), name='department_detail'),
#     path('department/create/',          DepartmentCreateView.as_view(), name='department_create'),
#     path('department/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department_update'),
#     path('department/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),

# #Comment
#     path('comment',                  CommentListView.as_view(),   name='all'),
#     path('comment/<int:pk>/detail',  CommentDetailView.as_view(), name='comment_detail'),
#     path('comment/create/',          CommentCreateView.as_view(), name='comment_create'),
#     path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
#     path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

# #Template
#     path('template',                  TemplateListView.as_view(),   name='all'),
#     path('template/<int:pk>/detail',  TemplateDetailView.as_view(), name='template_detail'),
#     path('template/create/',          TemplateCreateView.as_view(), name='template_create'),
#     path('template/<int:pk>/update/', TemplateUpdateView.as_view(), name='template_update'),
#     path('template/<int:pk>/delete/', TemplateDeleteView.as_view(), name='template_delete'),

# #HelpTopic
#     path('helpTopic',                  HelpTopicListView.as_view(),   name='all'),
#     path('helpTopic/<int:pk>/detail',  HelpTopicDetailView.as_view(), name='helpTopic_detail'),
#     path('helpTopic/create/',          HelpTopicCreateView.as_view(), name='helpTopic_create'),
#     path('helpTopic/<int:pk>/update/', HelpTopicUpdateView.as_view(), name='helpTopic_update'),
#     path('helpTopic/<int:pk>/delete/', HelpTopicDeleteView.as_view(), name='helpTopic_delete'),

# #Shift
#     path('shift',                  ShiftListView.as_view(),   name='all'),
#     path('shift/<int:pk>/detail',  ShiftDetailView.as_view(), name='shift_detail'),
#     path('shift/create/',          ShiftCreateView.as_view(), name='shift_create'),
#     path('shift/<int:pk>/update/', ShiftUpdateView.as_view(), name='shift_update'),
#     path('shift/<int:pk>/delete/', ShiftDeleteView.as_view(), name='shift_delete'),

# #Role
#     path('role',                  RoleListView.as_view(),   name='all'),
#     path('role/<int:pk>/detail',  RoleDetailView.as_view(), name='role_detail'),
#     path('role/create/',          RoleCreateView.as_view(), name='role_create'),
#     path('role/<int:pk>/update/', RoleUpdateView.as_view(), name='role_update'),
#     path('role/<int:pk>/delete/', RoleDeleteView.as_view(), name='role_delete'),

# #Status
#     path('status',                  StatusListView.as_view(),   name='all'),
#     path('status/<int:pk>/detail',  StatusDetailView.as_view(), name='status_detail'),
#     path('status/create/',          StatusCreateView.as_view(), name='status_create'),
#     path('status/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
#     path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),

# #Severity
#     path('severity',                  SeverityListView.as_view(),   name='all'),
#     path('severity/<int:pk>/detail',  SeverityDetailView.as_view(), name='severity_detail'),
#     path('severity/create/',          SeverityCreateView.as_view(), name='severity_create'),
#     path('severity/<int:pk>/update/', SeverityUpdateView.as_view(), name='severity_update'),
#     path('severity/<int:pk>/delete/', SeverityDeleteView.as_view(), name='severity_delete'),

# #Priority
#     path('priority',                  PriorityListView.as_view(),   name='all'),
#     path('priority/<int:pk>/detail',  PriorityDetailView.as_view(), name='priority_detail'),
#     path('priority/create/',          PriorityCreateView.as_view(), name='priority_create'),
#     path('priority/<int:pk>/update/', PriorityUpdateView.as_view(), name='priority_update'),
#     path('priority/<int:pk>/delete/', PriorityDeleteView.as_view(), name='priority_delete'),

]