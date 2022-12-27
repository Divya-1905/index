from django.db import models



Product_choice =[
       ('GROCEROY', 'groceroy'),
       ( 'STATENOERY','stateonery'),
        ('ELECTRONICS','electronics'),
        ('CLOTHING','clothing'),
        ('FURNITURE','furniture')
    ]

class products(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name 
quanity_choies=[
    ('grams','grams'),
    ('kilograms','kilograms')
]        
class Groceroy(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(blank=True,null=True)
    quanity = models.CharField(choices=quanity_choies,default=None,blank=True,max_length=30)
    def __str__(self):
        return self.name
stateonery_choices=[
    ('pen','pen'),
    ('books','books'),
    ('penclis','pencils'),
]        
class Stateonery(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(blank=True,null=True)
    items = models.CharField(choices=stateonery_choices,default=None,null=True,max_length=30)
    def __str__(self):
        return self.name
Electroncis_choics =[
    ('table','tabel'),
    ('chair','chair'),
    ('sofa','sofa'),
]
class Electronic(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(blank=True,null=True)
    items = models.CharField(choices=Electroncis_choics,default=None,null=True,max_length=30)
    def __str__(self):
        return self.name
Clothing_chocies=[
    ('M','Male'),
    ('F','Female')
]
class Clothing(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(blank=True,null=True)
    chocies = models.CharField(choices=Clothing_chocies,default=None,null= True,max_length=30)
    def __str__(self):
        return self.name
furiniture_choices=[
    ('table','tabel'),
    ('chair','chair'),
    ('sofa','sofa'),
]  
class Furiniture(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(blank=True,null=True)
    items = models.CharField(choices = furiniture_choices,default=None,null=True,max_length=30)
    def __str__(self):
        return self.name 
class consumer(models.Model):
    name = models.CharField(max_length=30)
    Address = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    Products_choice = models.CharField(choices=Product_choice,default=None,blank=True,null=True,max_length=30)
    def __str__(self):
        return self.phone

