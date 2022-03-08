from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

# A decorator for allowing superuser(user) to access the page..
def un_superuser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser == 1:
                return view_func(request, *args, **kwargs)
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group == 'admins':
                    return redirect('admindashboard_url')
                if group == 'observer':
                    return redirect('customerdashboard_url')
                if group == 'expert':
                    return redirect('expertdashboard_url')
            else:
                messages.info(request, 'Ur None A member')
                return redirect('login_url')
        else:
            return request('login_url')

    return wrapper_func

# A decorator for allowing admins(user) to access the page..
def un_admins(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser == 1:
                return redirect('../admin/')
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group == 'admins':
                    return view_func(request, *args, **kwargs)
                if group == 'observer':
                    return redirect('customerdashboard_url')
                if group == 'expert':
                    return redirect('expertdashboard_url')
            else:
                messages.info(request, 'Ur None A member')
                return redirect('login_url')
        else:
            return request('login_url')

    return wrapper_func

# A decorator for allowing an expert(user) to access the page..
def un_expert(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser == 1:
                return redirect('../admin/')
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group == 'admins':
                    return redirect('admindashboard_url')
                if group == 'observer':
                    return redirect('customerdashboard_url')
                if group == 'expert':
                    return view_func(request, *args, **kwargs)
            else:
                messages.info(request, 'Ur None A member')
                return redirect('login_url')
        else:
            return request('login_url')

    return wrapper_func

# A decorator for allowing an observer(user) to access the page..
def un_observer(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser == 1:
                return redirect('../admin/')
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group == 'admins':
                    return redirect('admindashboard_url')
                if group == 'observer':
                    return view_func(request, *args, **kwargs)
                if group == 'expert':
                    return redirect('expertdashboard_url')
            else:
                messages.info(request, 'Ur None A member')
                return redirect('login_url')
        else:
            return request('login_url')

    return wrapper_func


#page restriction that who is allowed to make changes to a specific page..
def allowed_roles(roles):
	def role(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.is_authenticated:
				if request.user.groups.exists():
					group = request.user.groups.all()[0].name
				if group == 'admin':
					if group == roles[0]:
						return view_func(request, *args, **kwargs)
					elif request.user.is_superuser == 1:
						return redirect('../../admin/')
					else:
						return redirect('customer_url')

				elif group == 'customer':
					if group == roles[0]:
						return view_func(request, *args, **kwargs)
					elif request.user.is_superuser == 1:
						return redirect('../../admin/')
					else:
						return redirect('board_url')
				else:
					return HttpResponse('you are not authorized')
			else:
				return redirect('login_url')
		return wrapper_func
	return role