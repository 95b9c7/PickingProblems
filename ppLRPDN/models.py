from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime
# Create your models here.
SUPPLIER_CHOICES = [
    ('Picking', 'Picking'),
    ('Setup', 'Setup'),
    ('Receiving', 'Receiving'),
    ('Production', 'Production'),
    ('Inventory Control', 'Inventory Control'),
]

defectChoices = [
    ('Dirty', 'Dirty'),
    ('Damaged', 'Damaged'),
    ('Wrong', 'Wrong'),
    ('Incomplete', 'Incomplete'),
    ('Excess', 'Excess'),
    ('Short', 'Short'),
    ('Expiration', 'Expiration'),
    ('Wrong UoM', 'Wrong UoM'),
    ('Other', 'Other'),
    ('WrngPrt', 'Wrong Part'),
    ('MxPrt', 'Mixed Part'),
    ('WrngQty', 'Wrong Quantity'),
    ('WrngLoc', 'Wrong Location'),
    ('Clearance', 'Clearance'),
    ('Photos', 'Photos'),
    ('Missing', 'Missing')
]

DEPARTMENT_CHOICES = [
    ('WRHS', 'Warehouse'),
    ('RTRN', 'Returns'),
    ('SHIP', 'Shipping'),
    ('INVC', 'InvControl'),
    ('PRNT', 'PrintRoom'),
    ('PRDN', 'Production'),
    ('CLNR', 'CleanRoom'),
    ('RCVG', 'Receiving'),
    ('STUP', 'SetUp'),
    # Add more departments as needed
]
APP_DEPT_CHOICES = [
    ('PCKN', 'Picking'),
    ('RTRN', 'Returns'),
    ('RUSH', 'Rushes'),
    ('INVC', 'InvControl'),
    ('PRDN', 'Production'),
    ('PTAW', 'PutAway'),
    ('RCVG', 'Receiving'),
    ('STUP', 'SetUp'),
    # Add more departments as needed
]

LINE_CHOICES = [

    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
    ('06', '06'),
    ('06A', '06A'),
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),  
]

SHIFT_CHOICES = [
    ('1', '1st'),
    ('2', '2nd'),
]

POD_CHOICES = [
    ('Production', 'Production'),
    ('Setup', 'Setup'),
    ('Planning', 'Planning'),
    ('Internal', 'Internal'),
]
class NewPickingProblem(models.Model):
    class Meta:
        permissions = [
            ("can_delete_pp", "Can delete picking problem"),
        ]
    reference_number = models.CharField(primary_key=True, max_length=12, unique=True, editable=False)  # CharField to store the reference number
    def save(self, *args, **kwargs):
        if not self.reference_number:
            # Generate the reference number based on the current date
            today = datetime.today()
            formatted_date = today.strftime('%y%m%d')
            
            # Find the highest existing reference number for today's date
            highest_today = NewPickingProblem.objects.filter(reference_number__startswith=formatted_date).order_by('-reference_number').first()
            
            if highest_today:
                # Increment the number part of the reference number
                last_number = int(highest_today.reference_number[-4:])
                new_number = last_number + 1
                reference_number = f"{formatted_date}-{new_number:04d}"
            else:
                # No existing reference numbers for today, start from 0001
                reference_number = f"{formatted_date}-0001"
            self.reference_number = reference_number
        super().save(*args, **kwargs)

    name = models.CharField(max_length=100) # Initial Fields
    date = models.DateField()
    time = models.TimeField()
    department = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES, default='-')
    line = models.CharField(max_length=5, choices=LINE_CHOICES, default='-')
    shift = models.CharField(max_length=1, choices=SHIFT_CHOICES, default='0')
    work_order = models.CharField(max_length=100, default='-')
    part_number = models.CharField(max_length=100, default='-')
    item_dsc = models.CharField(max_length=100, default='-')
    unit_type = models.CharField(max_length=100, default='-')
    defect = models.CharField(max_length=100,choices=defectChoices, default='-')
    total_count = models.IntegerField(default=0)
    total_affected = models.IntegerField(default=0)
    app_dept = models.CharField(max_length=4, choices=APP_DEPT_CHOICES, default='-')
    comment = models.CharField(max_length=200, default='-')
    def __str__(self):
        return self.work_order, self.reference_number
    employee_username = models.CharField(max_length=255, default='-')
    location = models.CharField(max_length=255, default='-')
    transaction_date = models.DateField(default='2001-01-01')
    transaction_time = models.TimeField(default='00:00:00')
    job_number = models.CharField(max_length=255, default='-')
    applied = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='-')
    root_cause = models.CharField(max_length=255, default='-')
    final_reason = models.CharField(max_length=255, default='-')
    final_comments = models.TextField(default='-')
    status = models.CharField(max_length=255, default='Pending')
    finalized = models.BooleanField(default=False)
    finalized_username = models.CharField(max_length=255, default='-')
    finalized_date = models.DateField(default='2001-01-01')
    finalized_time = models.TimeField(default='00:00:00')
    
class Ticket(models.Model):
    NON_CONFORMANCE_CHOICES = [
        ('W01', 'Dirty/damaged rejected product'),
        ('W02', 'Product not labeled'),
        ('W03', 'Missing item(s)'),
        ('W04', 'Mixed orders WOs/waves'),
        ('W05', 'Order missing'),
        ('W06', 'Picked over'),
        ('W07', 'Packaging'),
        ('W08', 'Received wrong item'),
        ('W09', 'Expired product'),
        ('W10', 'Picked short'),
        ('W13', 'Dirty work area e.g., picker, cart, etc.'),
        ('W14', 'Improper use of equipment (horn, etc.)'),
        ('W15', 'Failure to follow procedure/directions'),
        ('W18', 'Exposed product (not put away in bag)'),
        ('W19', 'Gross overage/shortage (75% or greater)'),
        ('W21', 'Trash found on location'),
        ('W22', 'Received wrong quantity'),
        ('W23', 'Failure to perform area clearance'),
        ('W24', 'Incorrect labeling of product'),
        ('W26', 'Missing expiration date'),
        ('W28', 'Received multiple lots under one lot number'),
        ('W29', 'Listed wrong expiration date'),
        ('W30', 'Incorrect lot number recorded'),
        ('W31', 'Overages not put away in boxes'),
        ('W32', 'Product found in wrong location'),
        ('W33', 'Product stocked too high to pick/cart from'),
        ('W34', 'Improper FIFO'),
        ('W35', 'Work order not updated'),
        ('W36', 'Improper documentation'),
        ('W37', 'Improper staging of product'),
        ('W38', 'Other (document other below)'),
        ('W39', 'Product found in trash'),
        ('W40', 'Picked wrong component'),
        ('W41', 'Missed transaction'),
        ('W42', 'Item left on location'),
        ('W43', 'Item stocked in wrong location'),
        ('W44', 'Safety violation'),
    ]
    ticket_number = models.AutoField(primary_key=True)
    employee_name = models.CharField("Employee Name", max_length=100)
    badge_number = models.CharField("Badge Number", max_length=20, blank=True, null=True)
    date = models.DateField("Date")
    location = models.CharField("Location", max_length=100)
    item_number = models.CharField("Item Number", max_length=50, blank=True, null=True)
    work_order = models.CharField("Work Order",max_length=50, blank=True, null=True)
    item_description = models.TextField("Item Description", blank=True, null=True)
    supplier = models.CharField("Supplier",choices=SUPPLIER_CHOICES,max_length=255, blank=True, null=True)
    point_of_discovery = models.CharField("Point of Discovery",choices=POD_CHOICES, max_length=200)
    badge_number_pod = models.CharField("Badge Number", max_length=20)
    non_conformances = MultiSelectField(choices=NON_CONFORMANCE_CHOICES, max_choices=len(NON_CONFORMANCE_CHOICES), max_length=3*len(NON_CONFORMANCE_CHOICES))
    lead_supervisor = models.CharField("Lead Supervisor",max_length=255, blank=True, null=True)
    investigation_date = models.DateField("Investigation Date",null=True, blank=True)
    training = models.BooleanField("Training",default=False)
    training_date = models.DateField("Date",null=True, blank=True)
    counseling = models.BooleanField("Counseling",default=False)
    counseling_date = models.DateField("Date",null=True, blank=True)
    disciplinary_action = models.BooleanField("Disciplinary Action",default=False)
    disciplinary_action_date = models.DateField("Disciplinary Action Date",null=True, blank=True)
    notes = models.TextField("Notes", blank=True, null=True)
    employee_signature = models.CharField("Employee Signature", max_length=100, null=True, blank=True)
    employee_signature_date = models.DateField("Date",null=True, blank=True)

    

class ActionLog(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    action_type = models.CharField(max_length=255)
    reference_number = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.action_type} {self.reference_number} on {self.timestamp}"
