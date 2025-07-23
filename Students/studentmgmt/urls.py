from django.urls import path


from studentmgmt import views

urlpatterns = [
    path('',views.students_list,name='students_list'),
    path('add/', views.students_create, name='students_create'),
    path('update/<int:roll_number>', views.student_update, name='student_update'),
    path('delete/<int:roll_number>', views.students_delete, name='student_delete'),

]