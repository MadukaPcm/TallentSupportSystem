from django.urls import path
from . import views

#path urls for expert app.
urlpatterns = [
    path('',views.DashboardView, name='expertdashboard_url'),
    path('account/', views.AccountView, name="account_url"),

    path('medialist/',views.MediaListView, name="medialists_url"),
    path('uploadmedia/', views.UploadMediaView.as_view(), name="uploadmedia_url"),
    path('editmedias/<str:pk>', views.EditMediasView, name="editmedias_urll"),
    path('viewmedia/<str:pk>',views.ViewMedia, name="viewmedias_url"),
    path('deletemedia/', views.DeleteMediaaView, name="deletemedia_urll"),
    path('listallmedias/',views.ListAllMediaView, name="listallmedias_url"),

    path('listfollowers/', views.ListFollowersView, name="listfollowers_url"),
    path('editfollower/', views.EditFollowerView, name="editfollower_urll"),
    path('followsupporter/',views.FollowSupportView, name="followsupporter_url"),
    path('report/', views.ReportView, name="report_url"),
]