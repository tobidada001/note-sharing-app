from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my-notes/', views.notes, name="notes"),
    path('add-new-note/', views.add_note_note, name="new_note"),
    path('register/', views.register, name="register"),
    path('login/', views.signin, name="signin" ),
    path('logout/', views.signout, name="logout" ),
    path('note/<str:username>/<slug:slug>/', views.view_note, name='view_note'),
    path('note/edit/<str:username>/<slug:slug>/', views.edit_note, name='edit_note'),

]
