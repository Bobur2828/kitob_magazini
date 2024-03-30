from django.db import models
from django.db import models


# Kitoblar uchun 
class Users(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    is_client = models.BooleanField(default=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='users')

    def __str__(self):
        return self.username


# Kitoblar uchun
class Book(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    avtor = models.CharField(max_length=255)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, default=None, null=True,
                              verbose_name='Profile_photo')
    print_date = models.DateField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True, upload_to='product')
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='books')
    literal = models.ForeignKey('Country', null=True, blank=True, on_delete=models.PROTECT, related_name='literal')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Kitob")
        verbose_name_plural = ("Kitoblar") 

# Kategoriyalar uchun
class Category(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)
    photo=models.ImageField(upload_to='cat_photos/%Y/%m/%d', blank=True, default=None,null=True, verbose_name='Category_photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Kategoriya")
        verbose_name_plural = ("kategoriyalar")

# Adabiyot turlari  yani many to many uchun
class Country(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)
    photo=models.ImageField(upload_to='country_photos/%Y/%m/%d', blank=True, default=None,null=True, verbose_name='Country_photo')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Davlator")
        verbose_name_plural = ("Davlatlar") 

# Mijozlar izohlari uchun 
class Izoh(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Izoh")
        verbose_name_plural = ("Izohlar")

# Saytdagi  kitob haqidagi aqllik gaplar uchun
class Status(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Status")
        verbose_name_plural = ("Statuslar")

# Pullik xizmatlar uchun 
class Obuna(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    content=models.TextField(max_length=300)
    content1=models.TextField(max_length=300)
    content2=models.TextField(max_length=300)
    content3=models.TextField(max_length=300)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Obuna")
        verbose_name_plural = ("Obunalar")