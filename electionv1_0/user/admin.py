from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

"""
UserCreationForm,
UserChangeForm
???
"""


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('citizenship_number', 'date_of_birth')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('citizenship_number', 'password','is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('citizenship_number', 'email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Demographic Details', {'fields': ('first_name',
                                            'middle_name',
                                            'last_name',
                                            'password',
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
                                            )}),
        ('Address Details', {'fields': ()}),
        ('Present Address', {'fields': ('present_state',
                                        'present_zone',
                                        'present_district',
                                        'present_rmm',
                                        'present_ward',
                                        'present_tole',
                                        'present_block',
                                        'present_contact',
                                        )}),
        ('Permanent Address', {'fields': ('permanent_state',
                                          'permanent_zone',
                                          'permanent_district',
                                          'permanent_rmm',
                                          'permanent_ward',
                                          'permanent_tole',
                                          'permanent_block',
                                          'permanent_contact',
                                          )}),
        ('Voting Details', {'fields': ('voting_state',
                                       'voting_district',
                                       'voting_rmm',
                                       'voting_ward',
                                       'voting_tole',
                                       'voting_booth',
                                       'voting_country',
                                       'email'
                                       )}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        ('Demographic Details', {
            'classes': ('wide',),
            'fields': ('first_name',
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
                       )}),
        ('Address Details', {'classes': ('wide',), 'fields': ()}),
        ('Present Address', {'classes': ('wide',),
                             'fields': ('present_state',
                                        'present_zone',
                                        'present_district',
                                        'present_rmm',
                                        'present_ward',
                                        'present_tole',
                                        'present_block',
                                        'present_contact',
                                        )}),
        ('Permanent Address', {'classes': ('wide',),
                               'fields': ('permanent_state',
                                          'permanent_zone',
                                          'permanent_district',
                                          'permanent_rmm',
                                          'permanent_ward',
                                          'permanent_tole',
                                          'permanent_block',
                                          'permanent_contact',
                                          )}),
        ('User Credentials', {'classes': ('wide',),
                              'fields': ('email',
                                         'password1',
                                         'password2',
                                         )}),
        ('Voting Details', {'classes': ('wide', 'extrapretty'),
                            'fields': ('voting_state',
                                       'voting_district',
                                       'voting_rmm',
                                       'voting_ward',
                                       'voting_tole',
                                       'voting_booth',
                                       'voting_country',
                                   
                                       )})
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
