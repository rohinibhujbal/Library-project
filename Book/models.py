from django.db import models

# Create your models here.
class BookActiveManeger(models.Manager):          #custom manager
    def get_queryset(self):
        return super(BookActiveManeger,self).get_queryset().filter(is_deleted='N')

class BookInActiveManeger(models.Manager):          #custom manager
    def get_queryset(self):
        return super(BookInActiveManeger,self).get_queryset().filter(is_deleted='Y')

class Book(models.Model):
    # id === by default-----django bydefoult creates an ids
    #colums will generate for below fields
    name = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    quantity =models.IntegerField()
    price = models.IntegerField() 
    is_published = models.BooleanField(default=False)
    is_deleted = models.CharField(max_length=1,default="N")

    #colums will not be generate for below fields
    active_objects = BookActiveManeger()
    inactive_objects = BookInActiveManeger()
    objects = models.Manager()    #mandatory

    def __str__(self):                 #to see the book name we use str()
        return f"{self.id}----{self.name}---{self.auther} "           

    class Meta:
        db_table = 'book_info'

# create table book(id int AUTO_INCREAMENT,name varchar(100),author varchar(100),quntity int,price float)

