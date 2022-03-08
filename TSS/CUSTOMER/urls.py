from django.urls import path
from . import views

#path urls for customer app.
urlpatterns = [
    path('',views.DashboardView, name="customerdashboard_url"),
    path('accountifo/',views.AccontInfoView, name="accountinfo_url"),
    
    path('mediafiles/',views.MediaFilesView, name="mediafiles_url"),
    path('followexpert/',views.FollowExpertView, name="followexpert_url"),
    path('expertresponse/',views.ExpertResponseView, name="expertresponse_url"),
    path('reportgeneration/', views.ReportGenerationView, name="reportgeneration_url"),
]
