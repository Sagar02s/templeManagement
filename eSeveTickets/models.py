from django.db import models

# Create your models here.
class Item(models.Model):
    # Primary Fields
    id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    item_name = models.CharField(max_length=100)  # Item name (varchar)
    
    # Stock fields
    p_stock = models.FloatField()  # Purchased stock (float)
    s_stock = models.FloatField()  # Sold stock (float)
    d_stock = models.FloatField()  # Damaged stock (float)
    t_stock = models.FloatField()  # Total stock (float)
    ps_stock = models.FloatField()  # Pending stock (float)
    ss_stock = models.FloatField()  # Stock in sale (float)
    dcsale_stock = models.IntegerField()  # Discounted sale stock (int)
    closing_stock = models.DecimalField(max_digits=15, decimal_places=2)  # Closing stock (decimal)

    # Price fields
    container = models.DecimalField(max_digits=15, decimal_places=2)  # Container cost (decimal)
    disc = models.DecimalField(max_digits=15, decimal_places=2)  # Discount (decimal)
    selling_price = models.FloatField()  # Selling price (float)
    mrp = models.FloatField()  # MRP (float)
    
    # Tax fields
    tax = models.DecimalField(max_digits=4, decimal_places=2)  # Tax 1 (decimal)
    tax_two = models.DecimalField(max_digits=4, decimal_places=2)  # Tax 2 (decimal)
    tax_three = models.DecimalField(max_digits=4, decimal_places=2)  # Tax 3 (decimal)
    cess = models.DecimalField(max_digits=4, decimal_places=2)  # Cess (decimal)
    
    # Other fields
    priority = models.CharField(max_length=100)  # Priority (varchar)
    unit = models.CharField(max_length=100)  # Unit (varchar)
    hsn_no = models.CharField(max_length=100)  # HSN number (varchar)
    image = models.ImageField(upload_to='images/')  # Image (file)
    enable = models.IntegerField()  # Enable status (int)
    stock_alert = models.IntegerField()  # Stock alert threshold (int)
    itemdetails = models.CharField(max_length=500)  # Item details (varchar)
    
    # Category field (added)
    category = models.CharField(max_length=25)  # Category field (varchar, length 25)
    
    # Extra fields (ext1, ext2, ..., ext8)
    ext1 = models.CharField(max_length=100, blank=True, null=True)  # Extra field 1 (varchar)
    ext2 = models.CharField(max_length=100, blank=True, null=True)  # Extra field 2 (varchar)
    ext3 = models.CharField(max_length=100, blank=True, null=True)  # Extra field 3 (varchar)
    ext4 = models.CharField(max_length=100, blank=True, null=True)  # Extra field 4 (varchar)
    ext5 = models.CharField(max_length=100, blank=True, null=True)  # Extra field 5 (varchar)
    ext6 = models.CharField(max_length=100, blank=True, null=True)  # Extra field 6 (varchar)
    ext7 = models.CharField(max_length=100, blank=True, null=True)  # Extra field 7 (varchar)
    ext8 = models.CharField(max_length=100, blank=True, null=True)  # Extra field 8 (varchar)
    
    # Localization
    language = models.CharField(max_length=250, blank=True, null=True)  # Language (varchar)
    
    # IDs
    to_id = models.IntegerField()  # Foreign key ID (int)
    dealer_cost = models.DecimalField(max_digits=10, decimal_places=2)  # Dealer cost (decimal)

    def __str__(self):
        return self.item_name
    

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    # Choices for radio buttons and dropdown
    CURRENCY_CHOICES = [
        ('₹', '₹ (Rupee)'),
        ('$','$(Dollar)'),
    ]
    
    MAINTAIN_CHOICES = [
        ('Accounts', 'Accounts'),
        ('Inventory', 'Inventory'),
    ]
    
    SERIAL_CHOICES = [
        ('General Accounts / Billing', 'General Accounts / Billing'),
        ('Without Serials', 'Without Serials'),
        ('With Serials', 'With Serials'),
    ]
    
    # Fields for the form
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    pincode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    currency_symbol = models.CharField(max_length=2, choices=CURRENCY_CHOICES)
    maintain = models.CharField(max_length=10, choices=MAINTAIN_CHOICES)
    financial_year = models.CharField(max_length=20)
    gstin = models.CharField(max_length=15)
    st = models.CharField(max_length=10)
    pan = models.CharField(max_length=10)
    cin_llp = models.CharField(max_length=20)
    serial_option = models.CharField(max_length=30, choices=SERIAL_CHOICES)
    purchase_date = models.DateField()
    sales_due = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.company_name