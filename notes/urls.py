from django.urls import path, include
from . import views
from .views import signup

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note_list'),
    path('note/<int:pk>/', views.note_detail_view, name='note_detail'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls'))

]
