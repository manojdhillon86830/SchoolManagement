from django.conf.urls import url
from schoolapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.viewStudent),
    path('view-students', views.viewStudent),
    path('edit-student',views.editStudent),
    path('delete-student',views.deleteStudent),
    path('new-student',views.newStudent),
    path(r'^add',views.add),
    path('edit',views.edit),
    path('login',views.userLogin),
    path('logout',views.userLogout),

]
