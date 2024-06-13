from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.db import models


class Location(models.Model):
    options = (
            ('district one','district one'),
            ('palm jumeirah','palm jumeirah'),
            ('downtown','downtown'),
            ('dubai marina','dubai marina'),
            ('dubai creek harbour','dubai creek harbour'),
            ('business bay','business bay'),
          )
    place = models.CharField(max_length=100,choices=options)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media/place_photo',null=True)
    def __str__(self) -> str:
         return self.place


class Properties(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    price = models.IntegerField()
    place = models.CharField(max_length=200)
    image = models.ImageField(upload_to='property_images')
    options=(
        ('apartments','apartments'),
        ('villas','villas'),
        ('townhouses','townhouses'),
    )
    types = (
         ('duplex','duplex'),
         ('penthouse','penthouse'),
    )
    company = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=100,choices=types,null=True,default='')
    is_off_plan = models.BooleanField(default=False)
    payment_plan = models.CharField(max_length=100)
    category = models.CharField(max_length=100,choices = options)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)
    map = models.CharField(max_length=500,null=True)
    video = models.CharField(max_length=500,null=True)
    def __str__(self) -> str:
        return self.title

class PaymentDetails(models.Model):
    on_booking = models.CharField(max_length=100,null=True)
    during_construction = models.CharField(max_length=100,null=True)
    upon_handover = models.CharField(max_length=100,null=True)
    property = models.OneToOneField(Properties,on_delete=models.CASCADE,related_name='payment_details',null=True)
    def __str__(self) -> str:
         return self.property.title
    
#Create a Payment details when Property is created
def create_payment_details(sender, instance, created, **kwargs):
	if created:
		payment_details = PaymentDetails(property=instance)
		payment_details.save()

# # Automate 
post_save.connect(create_payment_details, sender=Properties)

class PropertyDetails(models.Model):
    property = models.OneToOneField(Properties,on_delete=models.CASCADE,null=True,related_name='detail')
    location = models.CharField(max_length=200,null=True)
    project_name = models.CharField(max_length=200,null=True)
    developer = models.CharField(max_length=200,null=True)
    completion_date= models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
         return self.property.title    
#Create a Property details when Property is created
def create_property_details(sender, instance, created, **kwargs):
	if created:
		property_details = PropertyDetails(property=instance)
		property_details.save()

# # Automate 
post_save.connect(create_property_details, sender=Properties)


class News(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='news_photos/', blank=True)
    description = models.TextField()
    updated_time = models.TimeField()
    updated_date = models.DateField()
    photo_count = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.photo and self.photo_count < 15:
            self.photo_count += 1
        super().save(*args, **kwargs)