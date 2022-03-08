from django.shortcuts import render, redirect,get_object_or_404
from ACCOUNT.decolators import un_expert
from ADMINS.form import CreateMediaForm,EditMediaForm
from django.contrib import messages
from ADMINS.models import *
from django.contrib.auth.models import User,Group

#creating media files:
from django.views.generic.edit import CreateView
from django.urls import reverse
from ADMINS.models import Media
import datetime

# Create your views here.
#a function view for expert .
@un_expert
def DashboardView(request):

    context = {}
    return render(request, 'expert/dashboard.html',context)

#expert account view function.
def AccountView(request):
    # date = datetime.datetime.now()
    # ts = Transactions.objects.filter(User=request.user).aggregate(Sum('amount'))
    # ttt = Transactions.objects.filter(User=request.user)
    # names = User.objects.filter(username=request.user)
    context = {}
    return render(request, 'expert/account.html', context)

#expert media list view
def MediaListView(request):
    file = Media.objects.filter(user=request.user)

    context = {'data':file}
    return render(request, 'expert/medialist.html', context)

#an expert viewing just a single uploaed media.
def ViewMedia(request,pk):
    dataa = Media.objects.get(id=pk)

    context = {'mediaa':dataa}
    return render(request, 'expert/viewmedia.html', context)

#expert upload medias view function
class UploadMediaView(CreateView):
    model = Media
    fields = '__all__'
    template_name = 'expert/uploadmedia.html'

    def get_success_url(self):
        return reverse('medialists_url')

#expert edit medias view function
def EditMediasView(request, pk):

    datas = Media.objects.get(id=pk)
    editmedias = EditMediaForm(instance=datas)

    if request.method == 'POST':
        editmedias = EditMediaForm(request.POST,instance=datas)
        if editmedias.is_valid():
            editmedias.save()
            
            messages.info(request, 'Updated')
            return redirect('medialists_url')

        else:
            messages.info(request, 'something went wrong:')
            return redirect('medialists_url')


    context = {'editmedias':editmedias}
    return render(request, 'expert/editmedias.html', context)

#soft delete media files view.
def DeleteMediaaView(request):
    deletem = get_object_or_404(Media, pk =request.GET.get('media_id'))
    deletem.un_deleted = not deletem.un_deleted
    deletem.save()
    return redirect('medialists_url')

#expert listallmeedias uploaded in system.
def ListAllMediaView(request):
    files = Media.objects.all()

    context = {'datass':files}
    return render(request, 'expert/listallmedias.html', context)

#expert follower view function
def ListFollowersView(request):

    context = {}
    return render(request, 'expert/listfollower.html', context)

#expert follow the supporter function view.
def FollowSupportView(request):

    context = {}
    return render(request, 'expert/followsupporter.html', context)

#expert editing supporter function view.
def EditFollowerView(request):

    context = {}
    return render(request, 'expert/editfollower.html', context)

#expert report generation function view
def ReportView(request):

    context = {}
    return render(request, 'expert/report.html', context)
