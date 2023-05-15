from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class AppUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.RESTRICT, related_name='app_user')
    city = models.CharField(db_column="city", max_length=256, null=False, blank=False, default='Tel Aviv')
    neighborhood = models.CharField(db_column="neighborhood", max_length=256, null=True, blank=True)
    phone_number = models.CharField(db_column="phone_number", max_length=128, null=False, blank=False)

class Ad(models.Model):

    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    city = models.CharField(db_column="city", max_length=256, null=False, blank=False)
    neighborhood = models.CharField(db_column="neighborhood", max_length=256, null=True, blank=True)
    published_date = models.DateTimeField(db_column="published_date", null=True, blank=True)
    #is_available = # if all the items in the ad are not available
    title = models.CharField(db_column="title", max_length=256, null=False, blank=False)


    class Meta:
        db_table = 'ads'
        ordering = ['id']


class Category(models.Model):

    category_name = models.CharField(db_column="category_name", max_length=256, null=False, blank=False)
    category_image_url = models.URLField(db_column="category_image_url", max_length=2083, null=True, blank=True)

    class Meta:
        db_table = 'categories'
        ordering = ['id']

    def __str__(self):
        return self.category_name

class Neighborhood(models.Model):

    neighborhood_name = models.CharField(db_column="neighborhood_name", max_length=256, null=False, blank=False)


    class Meta:
        db_table = 'neighborhoods'
        ordering = ['id']



class City(models.Model):
    city_name = models.CharField(db_column="city_name", max_length=255, null=False, blank=False)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.city_name

    class Meta:
        db_table = 'cities'
        ordering = ['id']



GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('A', 'Agender')]
CONDITION_CHOICES = [('N', 'New'), ('E', 'Excellent'), ('G', 'Good'), ('F', 'Fair')]

class Item(models.Model):

    # user = models.ForeignKey(User, on_delete=models.RESTRICT)
    # city = models.CharField(db_column="city", max_length=256, null=False, blank=False)
    # neighborhood = models.CharField(db_column="neighborhood", max_length=256, null=True, blank=True)
    published_date = models.DateTimeField(db_column="published_date", null=True, blank=True)
    category = models.ForeignKey(Category,  on_delete=models.SET_NULL, null=True)
    ad = models.ForeignKey(Ad, on_delete=models.RESTRICT)
    title = models.CharField(db_column="title", max_length=256, null=False, blank=False)
    #todo: change size to age

    size = models.IntegerField(db_column="size", null=False, blank=False,
                               validators=[MinValueValidator(0), MaxValueValidator(16)])
    condition = models.CharField(db_column="condition", choices=CONDITION_CHOICES, max_length=32, null=True, blank=True)
    gender = models.CharField(db_column="gender", choices=GENDER_CHOICES, max_length=32, null=True, blank=True)
    #todo: change later to null=false
    image = models.TextField(db_column="image", null=True, blank=True, default="https://img.freepik.com/free-vector/baby-clothes-set_74855-202.jpg?w=2000")
    description = models.TextField(db_column='description', null=True, blank=True)
    is_interested = models.BooleanField(db_column="is_interested", null=True, blank=True)
    is_multiple = models.BooleanField(db_column="is_multiple", default=True, null=True, blank=True)
    collected_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collected_items', null=True, blank=True)

    class Meta:
        db_table = 'items'
        ordering = ['id']

class Interactions(models.Model):

    INTERACTIONS_CHOICES = [('Viewed', 'Viewed the item'), ('Contact', 'Contact'), ('Collected', 'Collected')]

    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    item = models.ForeignKey(Item, on_delete=models.RESTRICT)
    interaction_type = models.CharField(db_column="interaction_type", choices=INTERACTIONS_CHOICES, max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'interactions'
        ordering = ['id']
