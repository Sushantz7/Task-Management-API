from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    This CustomUserManager is required whenever the email is needed to be set as a unique identifier
    and username is not needed to create a user.
    Using this the authentication can be done using email rather than username.
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is mandatory.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        This is for creating the superuser using the email as unique identifier
        and username is not needed to create a user.

        """
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True.")

        return self.create_user(email, password, **extra_fields)
