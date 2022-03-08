from django.shortcuts import render,redirect,get_object_or_404
from ACCOUNT.decolators import un_admins
from ADMINS.models import *

#dealing with permissions to groups and users...
from django.contrib.auth.models import User,Group,Permission

#creating media files:
from django.views.generic.edit import CreateView
from django.urls import reverse
from ADMINS.models import Media

from django.contrib import messages
from ADMINS.form import AddUserDataForm,UserFollowerForm,UpdateUserForm,EditFollowerForm,CreateMediaForm,EditMediaForm,GroupFormPerm

# Create your views here.
#admin dashboard function view.
@un_admins
def DashboardView(request):

    context = {}
    return render(request, 'admin/dashboard.html',context)

#creating a user in admin side..
def CreateUserView(request):
    if request.method == 'POST':
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')
        usergroup = request.POST.get('Usergroup')

        if User.objects.filter(username = request.POST['Username']).exists():
            messages.info(request, "User already exists")
            return redirect('userlist_url')
        
        if len(username) < 5:
            messages.info(request,'usernae should have atleast 5 characters')
            return redirect('userlist_url')

        if User.objects.filter(email=request.POST['Email']).exists():
            messages.info(request,'email already taken')
            return redirect('userlist_url')

        if password1 != password2:
            messages.info(request,'password does not match')
            return redirect('register_url')

        if len(password1) != 8:
            messages.info(request, 'password, write 8 mixed characters')
            return redirect('register_url')

        else:
            userdata = User.objects.create_user(
                username = username,
                email = email,
                password = password1
            )
            userdata.first_name = First_name
            userdata.last_name = Last_name
            userdata.save()

            if usergroup == '1':
               group = Group.objects.get(name = 'expert')
               user = User.objects.get(username = username)
               user.groups.add(group)
            
               messages.info(request, "User Created.")
               return redirect('userlist_url')  

            else:
                group = Group.objects.get(name = 'observer')
                user = User.objects.get(username = username)
                user.groups.add(group)

                messages.info(request, "User Created.")
                return redirect('userlist_url')  
    else:
        return redirect('userlist_url')  

#admin user list function view.
def UserListView(request):
    # user = User.objects.filter(groups__name = ["observer","expert"])
    ser = User.objects.all()

    permgroup = request.user.get_all_permissions()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    
    context = {'userdata':ser, 'perm':permgroup}
    return render(request, 'admin/userlist.html', context)

# def EditUserView(request,pk):
#     usr = User.objects.get(id=pk)
#     UserForm = UpdateUserForm(instance = usr)

#     if request.method == 'POST':
#         UserForm = UpdateUserForm(request.POST, instance=usr)
#         if UserForm.is_valid():
          
#             UserForm.save()
#             messages.info(request, 'Data updated.')
#             return redirect('userlist_url')
        
#         else:
#             messages.info(request, 'sommething went wrong')
#             return redirect('edituser_url')

#     context = {'fm':UserForm}
#     return render(request,'admin/edituser.html',context)
#admin edit user function.
def EditUserView(request,pk):
    userform = User.objects.get(id=pk)

    if request.method == 'POST':
        id = request.POST.get('Id')
        first_name = request.POST.get('First_name')
        last_name = request.POST.get('Last_name')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        status = request.POST.get('Status')

        userdata = User.objects.create_user(id=id,password=password, email=email)
        userdata.first_name = first_name
        userdata.last_name = last_name
        userdata.is_active = status
        userdata.save()

        return redirect('userlist_url')

    context = {'userupdate':userform}
    return render(request,'admin/edituser.html',context)

# def DeleteUserView(request, pk):
#     us = User.objects.filter(id=pk).delete()
#     messages.info(request, "successfully deleted!!")
#     return redirect('userlist_url')

#soft delete..for the user.
def SoftDeleteView(request):
    dell = get_object_or_404(User,pk=request.GET.get('userlist_id'))
    dell.is_active = not dell.is_active
    dell.save()
    return redirect('userlist_url')
        

#Admin user informations
def UserDetailView(request):
    userdata = UserDetails.objects.all()

    context = {'userdata':userdata}
    return render(request, 'admin/userdetail.html', context)

def AddUserData(request):
    userd = User.objects.all()
    userdform = AddUserDataForm()
    
    if request.method == 'POST':
        userdform = AddUserDataForm(request.POST)
        if userdform.is_valid():
            userdform.save()

            messages.info(request, 'Details Added')
            return redirect('userdetail_url')

        else:
            messages.info(request, 'Invalid Credintials')
            return redirect('adduserdata_url')

    context = {'userdform':userdform}
    return render(request, 'admin/adduserdata.html',context)

#admin edit user detail or informations
def EditUserDetailView(request, pk):
    data = UserDetails.objects.get(id=pk)
    edituserdform = AddUserDataForm(instance=data)

    if request.method == 'POST':
        edituserdform = AddUserDataForm(request.POST, instance=data)
        if edituserdform.is_valid():
            edituserdform.save()

            messages.info(request, 'data updated:')
            return redirect('userdetail_url')

        else:
            messages.info(request, 'something went wrong:')
            return redirect('userdetail_url')

    context = {'edituserdform':edituserdform}
    return render(request, 'admin/edituserdetail.html',context)

#soft delete for user details...
def DeleteUserDetailView(request):
    deldata = get_object_or_404(UserDetails, pk=request.GET.get('userdata_id'))
    deldata.un_deleted = not deldata.un_deleted
    deldata.save()
    return redirect('userdetail_url')


#dealing with user groupo permissions.
def UserGroupView(request):
    datagroup = Group.objects.all()

    # for group in Group.objects.all():
    #     assigned = group.permissions.all()

    assigned = request.user.get_group_permissions()

    context = {'group':datagroup,'assignedp':assigned}
    return render(request,'admin/usergroup.html', context)

def AssignGroupPermView(request, pk):
    datas = Group.objects.get(id=pk)
    permassign = GroupFormPerm(instance=datas)

    if request.method == 'POST':
        permassign = GroupFormPerm(request.POST, instance=datas)
        if permassign.is_valid():
            permassign.save()

            return redirect('grouplist_url')

    context = {'perm':permassign}
    return render(request, 'admin/assigngroupperm.html',context)

#admin adding tallent names/choices.
def TallentView(request):
    tallents = Tallent.objects.all()

    context = {'name':tallents}
    return render(request, 'admin/tallent.html',context)

#add talent view.
def AddTallentView(request):

    if request.method == 'POST':
        name = request.POST.get('Name')
        tall = Tallent.objects.create(name=name)
        tall.save()

        return redirect('tallent_url')
    else:
        messages.info(request, 'Something went wrong')
        return redirect(request, 'tallent_url')

#soft delete tallent view.
def DeleteTallentView(request, pk):
    deltal = Tallent.objects.get(id=pk).delete()
    messages.info(request, 'Talent cat deleted:')

    return redirect('tallent_url')


#my account informations
def MyAccountView(request):

    context = {}
    return render(request, 'admin/myaccount.html', context)

#admin follower view function
def FollowerView(request):
    follower = Follower.objects.all()

    context = {'follower':follower}
    return render(request, 'admin/follower.html',context)

def AddFollowerView(request):
    followerform = UserFollowerForm

    if request.method == 'POST':
        followerform = UserFollowerForm(request.POST)
        if followerform.is_valid():
            followerform.save()

            messages.info(request, 'Expert Followed.')
            return redirect('follower_url')
        else:
            messages.info(request, 'something went wrong:')
            return redirect('follower_url')

    context = {'followerform':followerform}
    return render(request, 'admin/addfollower.html',context)

def EditFollowerView(request,pk):
    data = Follower.objects.get(id=pk)
    editfollowerform = EditFollowerForm(instance=data)

    if request.method == 'POST':
        editfollowerform = EditFollowerForm(request.POST, instance=data)
        if editfollowerform.is_valid():
            editfollowerform.save()

            messages.info(request, 'updated')
            return redirect('follower_url')

        else:
            messages.info(request, '00p Error')
            return redirect('follower_url')

    context = {'editfollowerform':editfollowerform}
    return render(request, 'admin/editfollower.html', context)

#delete follower view.
def DeleteFollowerView(request):
    delfollower = get_object_or_404(Follower,pk=request.GET.get('folll_id'))
    delfollower.un_deleted = not delfollower.un_deleted
    delfollower.save()
    return redirect('follower_url')

#admin dealing with media function view.
def MediaView(request):
    medias = Media.objects.all()

    context = {'medias':medias}
    return render(request,'admin/media.html', context)

#expert upload medias view function
class AddMediaView(CreateView):
    model = Media
    fields = ['user','title','description','video_file','thumbnail']
    template_name = 'admin/addmedia.html'
    
    def get_success_url(self):
        return reverse('media_url')

#editing media view..
def EditMediaView(request, pk):
    data = Media.objects.get(id=pk)
    editmedia = EditMediaForm(instance=data)

    if request.method == 'POST':
        editmedia = EditMediaForm(request.POST,instance=data)
        if editmedia.is_valid():
            editmedia.save()
            
            messages.info(request, 'Updated')
            return redirect('media_url')

        else:
            messages.info(request, 'something went wrong:')
            return redirect('media_url')


    context = {'editmedia':editmedia}
    return render(request, 'admin/editmedia.html', context)

def ViewMediaView(request, pk):
    data = Media.objects.get(id=pk)

    context = {'media':data}
    return render(request, 'admin/viewmedia.html', context)

#soft delete media view for an admin...
def DeleteMediaView(request):
    data = get_object_or_404(Media,pk=request.GET.get('mediaa_id'))
    data.un_deleted = not data.un_deleted
    data.save()

    messages.info(request, 'Media deleted')
    return redirect('media_url')

def ExpertReportView(request):

    context = {}
    return render(request, 'admin/expertreport.html', context)