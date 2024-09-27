"""External Imports"""
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.core.validators import RegexValidator

class UserData(AbstractUser):
    """
    Table for User Data
    """

    phone_regex = RegexValidator(
        regex=r"(0/91)?[6-9][0-9]{9}",
        message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.",
    )
    password_regex = RegexValidator(
        regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
        message="Minimum 8 character password including alphanumeric, special character and a Capital letter alphabet",
    )
    username = None
    phone = models.CharField(
        validators=[phone_regex],
        max_length=30,
        unique=True,
        null=True,
    )
    password = models.CharField(
        validators=[password_regex],
        max_length=20
    )


    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
        verbose_name="groups_"
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        verbose_name="user permissions"
    )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    USERNAME_FIELD = 'phone'  # Use 'phone' instead of 'username'
    REQUIRED_FIELDS = []

    def create_user(self, phone, password=None, **extra_fields):
        """Override create_user method to use phone instead of username"""
        if not phone:
            raise ValueError("The Phone number must be set")
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user