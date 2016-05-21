from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, first_name='Имя', last_name='', study_group='', password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Необходимо указать логин создаваемого пользователя')

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            study_group=study_group,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=100, default='', verbose_name="Логин", unique=True)
    first_name = models.CharField(max_length=100, default='', verbose_name="Имя")
    last_name = models.CharField(max_length=100, default='', verbose_name="Фамилия")
    study_group = models.CharField(max_length=100, default='', verbose_name="Группа")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    is_admin = models.BooleanField(default=False, verbose_name="Администратор")

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username