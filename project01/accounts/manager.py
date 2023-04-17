from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True


    # To Create Ordinary User
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("Email Is Required")
        
        # email normalization
        email = self.normalize_email(email)
        # creating object
        user  = self.model(email=email, **extra_fields)
        # Hashing password
        user.set_password(password)
        # Saving User Object In DataBase
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):

        # Set User As a Staff User
        extra_fields.setdefault('is_staff',True)
        # Set User As a SuperUser
        extra_fields.setdefault('is_superuser',True)
        # Set User As a Active User
        extra_fields.setdefault('is_active',True)

        # Check The Exception
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser Must Have 'is_staff' True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser Must Have 'is_superuser' True")
        if extra_fields.get('is_active') is not True:
            raise ValueError("Superuser Must Have 'is_active' True")
        
        # Create Object And Save UserObject In Database
        return self.create_user(email, password, **extra_fields)
