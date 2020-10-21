from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from user.views import UserLoginIndexView, main, IntakeView, ProgramView, PlanningList, PlanningListDetail, upload_file
from progression.views import  ProgressList, ProgressListDetail, CTRSList, CTRSListDetail, UpdateListView, UpdateView
from progression.views import ProgressUpdate, ProgressUpdateView, statistics, statistics_2019, statistics_2020, report
from counselor.views import UserRegistrationView, UserLoginView

# Media file improt
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserLoginIndexView.as_view(), name='index'),
    path('main/', main, name='main'),
    path('login/main/', main, name='main'),
    path('initial/', IntakeView.as_view(), name='initial'),
    path('setplan_list/', PlanningList.as_view(), name='setplan_list'),
    path('setplan_list/<int:pk>/', PlanningListDetail.as_view(), name='setplan_detail'),
    # path('setplan/', PlanningView.as_view(), name='setplan'),
    path('danger_list/', CTRSList.as_view(), name='danger_list'),
    path('danger_list/<int:pk>/', CTRSListDetail.as_view(), name='danger_detail'),
    # path('danger/', danger, name='danger'),
    path('getplan_list/', ProgressList.as_view(), name='getplan_list'),
    path('getplan_list/<int:pk>/', ProgressListDetail.as_view(), name='getplan_detail'),
    # path('getplan/', getplan, name='getplan'),
    path('perfor/', ProgramView.as_view(), name='perfor'),
    # urls about Login
    path('create/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    # path('update/<progress_id>/', UpdateDetailView.as_view()),
    path('update/<int:pk>/update/', ProgressUpdate.as_view(), name='update'),
    # upload & update
    path('upload/', upload_file, name='upload'),
    path('update/', UpdateListView.as_view(), name='update_list'),
    # statistics
    path('pivot/', statistics, name='pivot'),
    path('pivot_2019/', statistics_2019, name='pivot_2019'),
    path('pivot_2020/', statistics_2020, name='pivot_2020'),
    path('report/', report, name='report'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# Custom View Site link from admin Page 
admin.site.site_url = "/main" 
# admin.site.index_template = 're_main.html'