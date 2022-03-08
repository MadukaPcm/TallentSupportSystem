from django.shortcuts import render, redirect
from ACCOUNT.decolators import un_observer
from ADMINS.models import *

# Create your views here.
#a function view for customer dashboard.
@un_observer
def DashboardView(request):

    context = {}
    return render(request,'customer/dashboard.html',context)

#a function view for supporter account informations
def AccontInfoView(request):

    context = {}
    return render(request,'customer/accountinfo.html',context)

#a function view for list of media files uploaded by an expert
def MediaFilesView(request):
    dat = Media.objects.all()

    context = {'dat':dat}
    return render(request,'customer/mediafiles.html',context)

#a function view for a supporter to follow an expert
def FollowExpertView(request):

    context = {}
    return render(request,'customer/followexpert.html',context)

#a function view for response from an expert
def ExpertResponseView(request):

    context = {}
    return render(request,'customer/expertresponse.html',context)

#a function view for a supporter to generate report 
def ReportGenerationView(request):
    
    context = {}
    return render(request, 'customer/reportgeneration.html', context)



