from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=70, default="")
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000, default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to = "shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=50 , default="")
    email  = models.CharField(max_length=254 , default="")
    phone = models.CharField(max_length=50,default="")
    desc  = models.CharField(max_length=500 , default="")
    msg_date = models.DateField()

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length = 5000, default="")
    name = models.CharField(max_length = 100, default="")
    email = models.CharField(max_length = 100, default="")
    address = models.CharField(max_length = 200, default="")
    city = models.CharField(max_length = 50, default="")
    state = models.CharField(max_length = 50, default="")
    zip_code = models.CharField(max_length = 50, default="")
    phone = models.CharField(max_length = 10, default="")
    amount = models.IntegerField(default=0)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key = True)
    order_id= models.CharField(max_length = 10, default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

class Register(models.Model):
    register_id = models.AutoField(primary_key = True)
    username  = models.CharField(max_length=50 , default="")
    email  = models.CharField(max_length=254 , default="")
    password = models.CharField(max_length=500 , default="")

    def __str__(self):
        return self.email

    @staticmethod
    def isExists(email):
        try:
            if Register.objects.get(email=email):
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Register.objects.get(email=email)
        except:
            return False