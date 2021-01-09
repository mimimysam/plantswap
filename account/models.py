from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import urllib.request, ssl, requests
from decimal import Decimal

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, address, city, state, zip_code, birthday, password=None):
        if not email:
            raise ValueError("Users must provide an email to create an account.")
        if not first_name:
            raise ValueError("Users must provide full name to create an account.")
        if not last_name:
            raise ValueError("Users must provide full name to create an account.")
        if not address:
            raise ValueError("Users must provide a complete address to create an account.")
        if not city:
            raise ValueError("Users must provide a complete address to create an account.")
        if not state:
            raise ValueError("Users must provide a complete address to create an account.")
        if not zip_code:
            raise ValueError("Users must provide a complete address to create an account.")
        if not birthday:
            raise ValueError("Users must provide a birthday to create an account.")

        user =  self.model(
                email = self.normalize_email(email),
                username = username,
                first_name = first_name,
                last_name = last_name,
                address = address,
                city = city,
                state = state,
                zip_code = zip_code,
                birthday = birthday,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, first_name, last_name, address, city, state, zip_code, birthday, password):
        user =  self.create_user(
                email = self.normalize_email(email),
                username = username,
                first_name = first_name,
                last_name = last_name,
                address = address,
                city = city,
                state = state,
                zip_code = zip_code,
                birthday = birthday,
                password = password
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=False, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    birthday = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'address', 'city', 'state', 'zip_code', 'birthday']

    objects = MyAccountManager()

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        ssl._create_default_https_context = ssl._create_unverified_context
        address = "%s, %s, %s, %s" % (self.address, self.city, self.state, self.zip_code)
        location = address.replace(" ", "+")

        if not self.latitude or not self.longitude:
            self.latitude, self.longitude = self.geocode(location)

        super(Account, self).save(*args, **kwargs)

    def geocode(self, location):
        address = urllib.parse.quote_plus(location)
        request = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (location, settings.GOOGLE_API_KEY)
        response = requests.get(request)
        data = response.json()

        if data['status'] == 'OK':
            latitude = data['results'][0]["geometry"]["location"]["lat"]
            longitude = data['results'][0]["geometry"]["location"]["lng"]
            return Decimal(latitude), Decimal(longitude)