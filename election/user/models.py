from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager
                                        )

# User Manager
class UserManager(BaseUserManager):
    def create_user(self, citizenship_number, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            citizenship_number = citizenship_number,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, citizenship_number, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            citizenship_number = citizenship_number,
            email = email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# User model
class User(AbstractBaseUser):
    DISTRICT_CHOICES = (
        ('janakpur', 'Janakpur'),
        ('bhaktapur', 'Bhaktapur'),
        ('kathmandu', 'Kathmandu'),
        ('lalitpur', 'Lalitpur')
    )
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )

    # Demographic Details
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50)
    post = models.CharField(max_length=50, blank=True, null=True)
    citizenship_number = models.IntegerField(verbose_name='Citizenship Number', unique=True)
    citizenship_issued_district = models.CharField(max_length=50)
    passport_number = models.IntegerField(verbose_name='Passport Number', null=True)
    blood_group = models.CharField(max_length=6, blank=True)

    # Address Details
    # Present Address
    present_state = models.CharField(max_length=50)
    present_zone = models.CharField(max_length=50)
    present_district = models.CharField(max_length=255, choices=DISTRICT_CHOICES)
    present_rmm = models.CharField(max_length=255)
    present_ward = models.IntegerField(verbose_name='ward number', null=True, blank=True)
    present_tole = models.CharField(max_length=255)
    present_block = models.IntegerField(verbose_name='block number', null=True, blank=True)
    present_contact = models.CharField(max_length=15)

    # Permanent Address
    permanent_state = models.CharField(max_length=50)
    permanent_zone = models.CharField(max_length=50)
    permanent_district = models.CharField(max_length=255, choices=DISTRICT_CHOICES)
    permanent_rmm = models.CharField(max_length=255)
    permanent_ward = models.IntegerField(verbose_name='ward number', null=True, blank=True)
    permanent_tole = models.CharField(max_length=255)
    permanent_block = models.IntegerField(verbose_name='block number', null=True, blank=True)
    permanent_contact = models.CharField(max_length=15)

    # Voting Details
    voting_state = models.CharField(max_length=50)
    voting_district = models.CharField(max_length=255, choices=DISTRICT_CHOICES)
    voting_rmm = models.CharField(max_length=255)
    voting_ward = models.IntegerField(verbose_name='ward number', null=True, blank=True)
    voting_tole = models.CharField(max_length=255)
    voting_booth = models.IntegerField(verbose_name='booth number', null=True, blank=True)
    voting_country = models.CharField(max_length=255)
    voting_email = models.EmailField(verbose_name='email address', max_length=255)

    # Admin panel side
    email = models.EmailField(verbose_name='email address', max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()


    USERNAME_FIELD = 'citizenship_number'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return str(self.citizenship_number)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

