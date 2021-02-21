from django.db import models

# Create your models here.

    
     
Available_Size = (
    ('S', 'small'),
    ('M', 'medium'),
    ('L', 'large'),
  ('XL', 'extra large'),
)
Available_Color = (
    ('w','white'),
    ('b','black'),
    ('g','green'),
    ('y','yellow'),
)

Trasaction_status = (
    ('1', 'Done'),
    ('2', 'pending'),
    ('3', '--------'),
)
class Product(models.Model):
    """This models is used for Products Details."""
    # product_id = models.CharField(max_length=20)
    sku = models.CharField(max_length=100,null=True,blank=True)
    idsku = models.CharField(max_length=50,null=True,blank=True)
    vendor_product_id = models.CharField(max_length=50,null=True,blank=True)
    product_name = models.CharField(max_length=100)
    # supplier_id = models.CharField(max_length=100) # It will foregin key of supplier
    category_id = models.CharField(max_length=100)
    quantity_per_unit = models.IntegerField()
    unit_price = models.FloatField()
    msrp = models.CharField(max_length=100)
    available_size = models.CharField(max_length=3,choices=Available_Size)
    available_color = models.CharField(max_length=3,choices=Available_Color)
    size = models.CharField(max_length=100,null=True,blank=True)
    color = models.CharField(max_length=100,null=True,blank=True)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    unit_weight = models.IntegerField()
    unit_in_stock = models.IntegerField()
    unit_or_order = models.IntegerField()
    reorder_level = models.CharField(max_length=100,null=True,blank=True)
    product_availble = models.BooleanField(default=False)
    discount_availble = models.CharField(max_length=100,null=True,blank=True)
    current_order = models.CharField(max_length=100,null=True,blank=True)
    picture = models.ImageField(null=True,blank=True)
    ranking = models.IntegerField()
    note = models.TextField(max_length=200,null=True,blank=True)
    


class Customer(models.Model):
    """This model is used for customer"""
    # customer_id = models.CharField(max_length=10,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    customer_class = models.CharField(max_length=100,null=True,blank=True) # have doubt
    room = models.CharField(max_length=100,null=True,blank=True)
    building = models.CharField(max_length=100,null=True,blank=True)
    address1 = models.CharField(max_length=100,null=True,blank=True)
    address2 = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=10,null=True,blank=True)
    email = models.EmailField()
    voice_mail = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100)
    credit_card = models.CharField(max_length=15)
    credit_card_type_id = models.CharField(max_length=100)
    card_exp_month = models.IntegerField()
    card_exp_year = models.IntegerField()
    billing_address = models.CharField(max_length=250)
    billing_city = models.CharField(max_length=100)
    billing_region = models.CharField(max_length=100)
    billing_postal_code = models.CharField(max_length=100)
    billing_country = models.CharField(max_length=100)
    ship_address = models.CharField(max_length=250)
    ship_city = models.CharField(max_length=250)
    ship_region = models.CharField(max_length=250)
    ship_postal_code = models.CharField(max_length=100)
    ship_country = models.CharField(max_length=100)
    date_entered = models.DateTimeField(auto_now_add=True)
    
PAYMENT_MODE = (
    ('online', 'online'),
    ('offline', 'offline'),
)

class Suppliers(models.Model):
    """
    Supplier Model.
    """
    # supplier_id = models.CharField(max_length=100,null=True,blank=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    contact_fname = models.CharField(max_length=100,null=True,blank=True)
    contact_lname = models.CharField(max_length=100,null=True,blank=True)
    contact_title = models.CharField(max_length=100,null=True,blank=True)
    address1 = models.CharField(max_length=250,null=True,blank=True)
    address2 = models.CharField(max_length=250,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100,null=True,blank=True)
    fax = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField()
    url = models.URLField(max_length=200,null=True,blank=True)
    payment_mode = models.CharField(max_length=10,choices=PAYMENT_MODE)
    Discount_type = models.CharField(max_length=20,null=True,blank=True)
    types_goods = models.CharField(max_length=100,null=True,blank=True)
    notes = models.TextField(max_length=300,null=True,blank=True)
    discount_avaiable = models.BooleanField(default=False)
    current_order = models.CharField(max_length=100,null=True,blank=True) 
    logo = models.ImageField(null=True,blank=True,default='')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')
    size_url = models.CharField(max_length=100,null=True,blank=True)
    

class Category(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    Category_id = models.CharField(max_length=100,null=True,blank=True)
    category_name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(max_length=300,null=True,blank=True)
    picture = models.ImageField(null=True,blank=True)
    active = models.BooleanField(default=False)
    
class Shipper(models.Model):
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)


class Order(models.Model):
    # order_id = models.CharField(max_length=50,null=True,blank=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')
    order_number = models.CharField(max_length=100,null=True,blank=True)
    payment_id = models.CharField(max_length=50,null=True,blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    ship_date = models.DateTimeField(default='')
    required_date = models.DateField()
    shipper_id = models.ForeignKey(Shipper, on_delete=models.CASCADE, db_column='shipper_id')
    freight = models.CharField(max_length=100,null=True,blank=True)
    sale_tax = models.CharField(max_length=100,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_status = models.CharField(max_length=1,choices=Trasaction_status)
    error_lock = models.CharField(max_length=100,null=True,blank=True)
    error_msg = models.CharField(max_length=100,null=True,blank=True)
    fullfiled = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)
    
    
class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    payment_type = models.CharField(max_length=10,choices=PAYMENT_MODE)
    allowed = models.BooleanField(default=False)
    
    
class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.DO_NOTHING, db_column='order_id')
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='product_id')
    order_number = models.CharField(max_length=100,null=True,blank=True)
    payment_id = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    quatity = models.IntegerField()
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    total = models.IntegerField()
    idsku = models.CharField(max_length=100,null=True,blank=True)
    size = models.CharField(max_length=3,choices=Available_Size)
    color = models.CharField(max_length=3,choices=Available_Color)
    fullfield = models.BooleanField(default=False)
    bill_date = models.DateField(default='')    
    
    
    
    