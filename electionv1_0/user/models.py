from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, citizenship_number, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        # if not email:
        #     raise ValueError('Users must have an email address')

        user = self.model(
            citizenship_number=citizenship_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, citizenship_number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            citizenship_number=citizenship_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )


    DISTRICT_CHOICES = (
        
        ('dolakha', 'Dolakha'),
        ('bhaktapur', 'Bhaktapur'),
        ('kathmandu', 'Kathmandu'),
        ('lalitpur', 'Lalitpur')
    )

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )

    ZONE_CHOICES = (
        ('janakpur', 'Janakpur'),
        ('bagmati', 'Bagmati')
    )

    # Demographic Details
    first_name = models.CharField(max_length=50,)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    mothers_name = models.CharField(verbose_name="Mother's Name", max_length=50)
    fathers_name = models.CharField(verbose_name="Father's Name", max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True)
    education = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50,blank=True, null=True)
    post = models.CharField(max_length=50, blank=True, null=True)
    citizenship_number = models.CharField(verbose_name='Citizenship Number', max_length=20, null=True, unique=True)
    citizenship_issued_district = models.CharField(max_length=50, choices=DISTRICT_CHOICES)
    passport_number = models.IntegerField(verbose_name='Passport Number', null=True, blank=True)
    blood_group = models.CharField(max_length=6, blank=True, null=True)

    # Address Details
    # Present Address
    present_state = models.CharField(verbose_name='State', max_length=50)
    present_zone = models.CharField(verbose_name='Zone', max_length=50, choices=ZONE_CHOICES)
    present_district = models.CharField(verbose_name='District',max_length=255, choices=DISTRICT_CHOICES)
    present_rmm = models.CharField(verbose_name='Rural Muncipality/ Muncipality',max_length=255)
    present_ward = models.IntegerField(verbose_name='Ward No.', null=True)
    present_tole = models.CharField(verbose_name='Tole',max_length=255)
    present_block = models.IntegerField(verbose_name='Block No.', null=True, blank=True)
    present_contact = models.CharField(verbose_name='Contact No.',max_length=15)

    # Permanent Address
    permanent_state = models.CharField(verbose_name='State', max_length=50)
    permanent_zone = models.CharField(verbose_name='Zone', max_length=50, choices=ZONE_CHOICES)
    permanent_district = models.CharField(verbose_name='District', max_length=255, choices=DISTRICT_CHOICES)
    permanent_rmm = models.CharField(verbose_name='Rural Muncipality/ Muncipality', max_length=255)
    permanent_ward = models.IntegerField(verbose_name='Ward No.', blank=True, null=True)
    permanent_tole = models.CharField(verbose_name='Tole', max_length=255)
    permanent_block = models.IntegerField(verbose_name='Block No.', null=True, blank=True)
    permanent_contact = models.CharField(verbose_name='Contact No.',max_length=15)

    # Voting Details
    voting_state = models.CharField(verbose_name='State', max_length=50)
    voting_district = models.CharField(verbose_name='District', max_length=255, choices=DISTRICT_CHOICES)
    voting_rmm = models.CharField(verbose_name='Rural Muncipality/ Muncipality', max_length=255)
    voting_ward = models.IntegerField(verbose_name='Ward No.', blank=True, null=True)
    voting_tole = models.CharField(verbose_name='Tole', max_length=255)
    voting_booth = models.IntegerField(verbose_name='Booth No.', blank=True, null=True)
    voting_country = models.CharField(verbose_name='Country', max_length=255)
    email = models.EmailField(verbose_name='Email Address', max_length=255)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'citizenship_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

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

    # @property
    # def is_active(self):
    #     "Is the user active?"
    #     # # Simplest possible answer: Yes, always
    #     return self.is_active