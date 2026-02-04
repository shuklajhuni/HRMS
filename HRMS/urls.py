from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from ess.views import (
    JSCodeLoginView,
    HRMSDashboardView,
    SelectionDashboardView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeHistoryView,
    HRAnalyticsView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', JSCodeLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('select/', SelectionDashboardView.as_view(), name='selection-dashboard'),
    path('hrms/', HRMSDashboardView.as_view(), name='hrms-dashboard'),

    path('hrms/employee', EmployeeCreateView.as_view(), name='employee-manage'),
    path('hrms/employee/edit/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-edit'),
    path('hrms/employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('hrms/employee/history/', EmployeeHistoryView.as_view(), name='employee-history'),
    path('hrms/analytics/', HRAnalyticsView.as_view(), name='hr-analytics')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)