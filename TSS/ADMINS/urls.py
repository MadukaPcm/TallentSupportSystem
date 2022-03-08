from django.urls import path
from . import views

#path urls for admins app.
urlpatterns = [
    path('',views.DashboardView, name='admindashboard_url'),
    path('createuser/',views.CreateUserView, name='RegisterFunction_urll'),
    path('userlist/',views.UserListView, name="userlist_url"),
    path('edituser/<str:pk>',views.EditUserView, name="edituser_url"),
    path('deleteuser/', views.SoftDeleteView, name='deleteuser_url'),

    #User group permissions management...
    path('grouppermission/', views.UserGroupView, name='grouplist_url'),
    path('AssignGroupPerm/<str:pk>', views.AssignGroupPermView, name='AssignGroupPerm_url'),

    #dealing with user details.... for an expart.
    path('userdetail/',views.UserDetailView, name="userdetail_url"),
    path('adduserdata/',views.AddUserData, name='adduserdata_url'),
    path('edituserdetail/<str:pk>',views.EditUserDetailView, name="edituserdetail_url"),
    path('deleteuserdata/',views.DeleteUserDetailView, name='deleteuserdata_url'),

    

    #dealing with tallent...
    path('tallent/', views.TallentView, name="tallent_url"),
    path('addtallent/', views.AddTallentView, name="addtallent_url"),
    path('deletetallent/<str:pk>', views.DeleteTallentView, name="deletetallent_url"),

    #admin dealing with expert followers.
    path('follower/',views.FollowerView, name="follower_url"),
    path('addfollower/', views.AddFollowerView, name="addfollower_url"),
    path('editfollower/<str:pk>', views.EditFollowerView, name="editfollower_url"),
    path('deletefollower/',views.DeleteFollowerView, name="deletefollower_url"),
    path('myaccount/', views.MyAccountView, name="myaccount_url"),

    #admin daeling with media files..
    path('media/', views.MediaView, name="media_url"),
    path('addmedia/', views.AddMediaView.as_view(), name='addmedia_url'),
    path('editmedia/<str:pk>', views.EditMediaView, name="editmedia_url"),
    path('viewmedia/<str:pk>', views.ViewMediaView, name="viewmedia_url"),
    path('deletemedia/', views.DeleteMediaView, name='deletemedia_url'),
    path('expertreport/', views.ExpertReportView, name="expertreport_url"),
]