from django import forms
from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'mothers_name',
                  'fathers_name',
                  'gender',
                  'date_of_birth',
                  'education',
                  'occupation',
                  'post',
                  'citizenship_number',
                  'citizenship_issued_district',
                  'passport_number',
                  'blood_group',
                  'present_state',
                  'present_zone',
                  'present_district',
                  'present_rmm',
                  'present_ward',
                  'present_tole',
                  'present_block',
                  'present_contact',
                  'permanent_state',
                  'permanent_zone',
                  'permanent_district',
                  'permanent_rmm',
                  'permanent_ward',
                  'permanent_tole',
                  'permanent_block',
                  'permanent_contact',
                  'voting_state',
                  'voting_district',
                  'voting_rmm',
                  'voting_ward',
                  'voting_tole',
                  'voting_booth',
                  'voting_country',
                  'email',

                  'password',
                  'confirm_password',
                  )

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
