from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/',index,name='ind'),
    path('master/',master,name='master'),
    path('thoughts/',thought,name='thought'),
    path('strategy/',strategy,name='strat'),
    path('view_report/<str:pk>/',report,name='rep'),
    path('',loginmanager,name='login'),
    path('logout/',logoutUser,name='log'),
    path('register/',addemp,name='add'),
    path('addstrategy/<str:pk>/',addstg,name='addstg'),
    path('empl_strategy_details/<str:pk>/',emplst,name='emplst'),
    path('edit_thought/<pk>/',edittho,name='edittho'),
    path('listemp/',listemp,name='list'),
    path('operation/',opera,name="opera"),
    path('addoperations/<str:pk>/',addopera,name='addopera'),
    path('empl_Operation_details/<str:pk>/',emplop,name='emplop'),
    path('editemployee/<str:pk>/',edit, name='edit'),
    # path('download/<filename>',download_file,name='download_file'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
