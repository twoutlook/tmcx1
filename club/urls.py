from django.urls import path
from . import views
app_name = 'club'

urlpatterns = [
    path('<int:pk>/', views.club_pk, name='club_pk'),
    path('<int:pk>/<int:clubdate>/attd/', views.club_pk_clubdate_attd, name='club_pk_clubdate_attd'),
    path('<int:pk>/<int:clubdate>/attdrole/', views.club_pk_clubdate_attdrole, name='club_pk_clubdate_attdrole'),
    path('<int:pk>/<int:clubdate>/role/', views.club_pk_clubdate_role, name='club_pk_clubdate_role'),

    path('meeting/new/', views.meeting_new, name='meeting_new'),
    path('meeting/<int:pk>/', views.meeting_detail, name='meeting_detail'),
    path('meeting/<int:pk>/edit/', views.meeting_edit, name='meeting_edit'),
    path('s1/', views.s1, name='s1'),
    path('rolecnt/', views.rolecnt, name='rolecnt'),
    path('rolecnt/<date1>/', views.rolecnt_date, name='rolecnt_date'),
    path('headcnt/', views.headcnt, name='headcnt'),
    path('headcnt/<date1>/', views.headcnt_date, name='headcnt_date'),
    path('best/', views.best, name='best'),
    path('s1/<date1>/', views.s1_date, name='s1_date'),
    path('s2/', views.s2, name='s2'),
    path('s3/', views.s3, name='s3'),
    path('s4/', views.s4, name='s4'),
    path('s2/<name>/', views.s2_name, name='s2_name'),
    # path('b1/<int:yr>/<int:mo>/', views.b1, name='b1'),
    # path('b1/', views.b1_list, name='b1_list'),
    # path('a2/', views.a2, name='a2'),
    # path('a3/', views.a3, name='a3'),
    
    # path('a1v2/', views.a1v2, name='a1v2'),
    # path('a2v2/', views.a2v2, name='a2v2'),
    # path('a3v2/', views.a3v2, name='a3v2'),
    # path('a4v2/', views.a4v2, name='a4v2'),
    
    # path('a8/', views.a8, name='a8'),
    # # path('init_ww/', views.init_ww, name='init_ww'),
    # path('ww2/', views.ww2, name='ww2'),
    
    path('', views.index, name='index'),
]