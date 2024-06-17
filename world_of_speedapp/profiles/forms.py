from django import forms

from world_of_speedapp.profiles.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {'password': forms.PasswordInput}
        help_texts = {'age': "Age requirement: 21 years and above."}


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {'password': forms.PasswordInput}
