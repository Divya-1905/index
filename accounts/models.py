from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,UserManager
from django.utils import timezone
from django.contrib.auth.hashers import make_password


        
class MyUsermanager(UserManager):
    def create_user(self,name,password,phone,email):
        if not phone:
            try:
                phone =int(phone)
            except:
                raise ValueError({'phone must be interger'})
        if not email:
            raise ValueError({'email is requried'})
        data = self.model(email=self.normalize_email(email))
        data.name = name
        data.phone = phone
        data.save(using=self._db)
        return data
    def create(self,phone,email,name):
        user = self._create(phone,email,name)
        user.save()
        return user
    def create_superuser(self,phone,email,name):
        user = self._create(phone=phone,email=email,name=name)
        user.is_admin=True
        user.save()
        return user  


class User(AbstractBaseUser):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
   
    created_at = models.DateField(auto_now_add=True)
    objects= MyUsermanager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']
    class Meta:
        ordering =['created_at']
    def save(self,*args, **kwargs):
        self.password = make_password(self.password)  #encripte the password encript the password
        return super().save(*args,**kwargs) #defalut pass value is changed is a have  password it become encritped
                         

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
# class baseuser(BaseUserManager):
#     def create_user(self,name,email,phone,address,date_of_birth):
#         if not phone:
#            try:
#                phone = int(phone)
#            except:
#                raise ValueError('numbers are only intergers')
#            raise ValueError('phone field is must')
#         if not email:
#            raise ValueError('email field is requried')
#         user.name = name
#         user = self.model(email=self.normalize_email(email))
#         user.phone = phone
#         user.date_of_birth = date_of_birth
#         user.address = address
#         user.save(using=self.db)
#         return user
#     def create_superuser(self,name,email,user_type,phone,adress): 
#         user = self.create_user(email=email,name=name,phone=phone,address=adress,user_type= user_type)
#         if user_type=='is_admin':
#             user.user_type = 'is_admin'
#         user.save(using = self.db)
#         return user  
# user_type_choices =(
#     ('is_admin','is_admin'),
#     ('is_custamer','is_customer'),
# )    
# class User(AbstractBaseUser):
#     name = models.CharField(max_length=20)
#     email = models.EmailField(unique=True)
#     adress = models.CharField(max_length=50)
#     phone = models.IntegerField(max_length=10)
#     user_type = models.CharField(max_length=25,choices=user_type_choices,blank=True,default=None    
#     )
#     created_at = models.DateTimeField(default=timezone.now)   
#     data = baseuser()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone']
#     @property
#     def is_custamer(self):
#         return self.user_type == 'is_customer' or self.user_type == 'is_admin'

#     @property
#     def is_admin(self):
#         return self.user_type == 'is_admin'

#     class Meta:
#         ordering = ('created_at')   
# class User(models.Model):
#     name = models.CharField(max_length=20)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=15,default=None,blank=True,null=True)
    
#     def save(self, *args, **kwargs):
#         password = make_password(self.password)
#         password.save(using= self.db)
#         return User
#         # super(User, self).save(*args, **kwargs)
# class MyUserBaseManager(BaseUserManager):
#     def create_user(self,name,phone,password,email):
#         if not phone:
#             try:
#                 phone = int(phone)
#             except:
#                 raise ValueError('number only a interger fields')
#         if not email:
#             raise ValueError('email is must be requried')
#         user = self.model(email=self.normalize_email(email))
#         user.name = name 
#         user.phone = phone
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user



# class signup(models.Model):
#     name = models.CharField(max_length=20)
#     password = models.CharField(max_length=10,blank=True)
#     def __str__(self):
#         password = make_password(self.request.data['password'])
#         return self.name
# class login(models.Model):
#     name = models.CharField(max_length=20)
#     password = models.CharField(max_length=10,unique=True,blank=True)
#     def __str__ (self):
#         # return self.name   