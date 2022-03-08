from django.db.models import Model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from ADMINS.models import *


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','is_active']

class GroupFormPerm(ModelForm):
    class Meta:
        model = Group
        fields = ['name','permissions']

class AddUserDataForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['user','Tallent','artist_name','artist_name','sex','phone','region','district','street','office_name']

        def clean(self):
            cleaned_data = super(AddUserDataForm,self).clean()

            sex = self.cleaned_data.get('sex')
            phone = self.cleaned_data.get('phone')

            if sex != 'male' or sex != 'female':
                self._errors['sex'] = self.error_class(['write male or female'])

            if len(phone) != 10:
                self._errors['phone'] = self.error_class(['phoneNo should have only 10 numbers'])

            return self.cleaned_data

class UserFollowerForm(ModelForm):
    class Meta:
        model = Follower
        fields = ['user','Media','phone','status']

#edit follower
class  EditFollowerForm(ModelForm):
    class Meta:
        model = Follower
        fields = ['user','Media','phone','status']

#form for creating media files.
class CreateMediaForm(ModelForm):
    class Meta:
        model = Media
        fields = ['user','title','description','video_file','thumbnail']

class EditMediaForm(ModelForm):
    class Meta:
        model = Media
        fields = ['user','title','description','video_file','thumbnail']



