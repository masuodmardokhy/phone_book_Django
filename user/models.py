from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, phone, password):
        if not email:
            raise ValueError('plz email')
        if not username:
            raise ValueError('plz username')
        if not phone:
            raise ValueError('phone')
        user = self.model(email=self.normalize_email(email), username=username, phone=phone)  #normalize  @ را به کوچک تبدیل کن .یعنی تمام حروف بعد از
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, phone, password):
        user = self.create_user(email, username, phone, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']
    objects = UserManager()   #بخاطر اینکه کلاس با این مدل رو بشناسد

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):    # What users are allowed to the admin panel?
        return self.is_admin



