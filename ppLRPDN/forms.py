from django import forms
from datetime import datetime
from .models import NewPickingProblem, Ticket
from django.contrib.auth.models import User

# Define department choices as a list of tuples (value, display_name)
FINAL_REASON_CHOICES = [
    ('', '-'),
    ('Mixed', 'Mixed Parts'),
    ('Wrong', 'Wrong'),
    ('Lost in Setup', 'Lost in Setup'),
    ('Picked Extra', 'Picked Extra'),
    ('Origin Change', 'Origin Change'),
    ('Incomplete Component','Incomplete Component'),
    ('Excess Picking', 'Excess Picking'),
    ('Damaged/Dirty', 'Damaged/Dirty Component'),
    ('Production Error', 'Production Error'),
    ('Pick Location', 'Wrong Pick Location'),
    ('Picked Short', 'Picked Short'),
    ('Other', 'Other')
]

ROOT_CAUSE_CHOICES = [
    ('', '-'),
    ('Pick Location', 'Wrong Pick Location'),
    ('Mixed', 'Mixed Parts'),
    ('Filling', 'Incorrect Filling'),
    ('Return', 'Return'),
    ('Supplier', 'Supplier'),
    ('Origin', 'Origin'),
    ('Employee', 'Employee'),
    ('Other', 'Other')
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

SUPPLIER_CHOICES = [
    ('Picking', 'Picking'),
    ('Setup', 'Setup'),
    ('Receiving', 'Receiving'),
    ('Production', 'Production'),
    ('Inventory Control', 'Inventory Control'),
]

class npp_form(forms.ModelForm):
    department = forms.ChoiceField(label='Reporting Department', choices=DEPARTMENT_CHOICES)
    class Meta:
        model = NewPickingProblem
        exclude = ['reference_number', 'job_number']  # Exclude the reference_number field
        fields = ['name', 'date', 'time', 'department', 'line', 'shift',
                   'work_order', 'part_number', 'item_dsc', 'unit_type', 
                   'total_count', 'total_affected', 'app_dept', 'defect',
                   'comment']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].initial = user.username
        self.fields['date'].initial = datetime.now().date()
        self.fields['time'].initial = datetime.now().time()

        # Make name, date, and time fields hidden but required
        self.fields['name'].widget = forms.HiddenInput()
        self.fields['date'].widget = forms.HiddenInput()
        self.fields['time'].widget = forms.HiddenInput()

    line = forms.ChoiceField(label='Line', choices=LINE_CHOICES)
    shift = forms.ChoiceField(label='Shift', choices=SHIFT_CHOICES)

    app_dept = forms.ChoiceField(label='Department Applied to', choices=APP_DEPT_CHOICES)
    defect = forms.ChoiceField(label='Defect', choices=defectChoices, widget=forms.RadioSelect(attrs={"class": "inline li"}))
    
    work_order = forms.CharField(label='Work Order')
    part_number = forms.CharField(label='Part Number')
    item_dsc = forms.CharField(label='Item Description')

    unit_type = forms.CharField(label='Unit of Measure')
    total_count = forms.IntegerField(label='Total Count')
    total_affected = forms.IntegerField(label='Total Affected')
    comment = forms.CharField(label='Comment', widget=forms.Textarea(attrs={'rows': 4, 'cols': 140}), required=False)

class fpp_form(forms.ModelForm):
    class Meta:
        model=NewPickingProblem
        exclude = ['reference_number']
        fields = ['employee_username', 'location', 'transaction_date',
                    'transaction_time', 'applied', 'root_cause', 'final_reason',
                    'final_comments', 'status', 'finalized', 'finalized_date', 'finalized_username']
        
    employee_username = forms.CharField(label='Employee Username', required=True)
    location = forms.CharField(label='Location', required=True)
    transaction_date = forms.DateField(label='Transaction Date', required=True)    
    transaction_time = forms.TimeField(label='Transaction Time', required=False)    
    applied = forms.ChoiceField(label='Applies?', choices=[('Y', 'Yes'), ('N', 'No')], required=False)
    root_cause = forms.ChoiceField(label='Root Cause', choices=ROOT_CAUSE_CHOICES, required=True)
    final_reason = forms.ChoiceField(label='Final Reason', choices= FINAL_REASON_CHOICES, required=True)    
    final_comments = forms.CharField(label='Final Comments', widget=forms.Textarea(attrs={'rows': 4, 'cols': 70}), required=False) 
    status = forms.CharField(label='Status', required=False)
    finalized = forms.BooleanField(label='Finalize?', required=True)
    finalized_date=forms.DateField(label='Finalized Date', required=False)   
    finalized_username=forms.CharField(label='Finalized Username', required=False)

    

class edit_fpp_form(forms.ModelForm):
    class Meta:
        model=NewPickingProblem
        exclude = ['reference_number']
        fields = ['defect', 'total_count', 'total_affected', 'comment', 'unit_type']
    
    defect = forms.ChoiceField(label='Defect', choices=defectChoices)
    total_count = forms.IntegerField(label='Total Count')
    total_affected = forms.IntegerField(label='Total Affected', widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}))
    unit_type = forms.CharField(label='Unit of Measure')
    comment = forms.CharField(label='Comment', widget=forms.Textarea(attrs={'rows': 4, 'cols': 30}))
    
class mpr_form(forms.Form):
    finalized = forms.ChoiceField(label='Finalized?', choices=[('','-'),('Y','Finalized'),('N','Pending')], required=False)
    status = forms.ChoiceField(label='Status', choices=[('','-'),('Y','Yes'),('N','No')], required=False)
    applied = forms.ChoiceField(label='Applied?', choices=[('','-'),('Y','Yes'),('N','No')], required=False)
    app_dept = forms.ChoiceField(label='Department Responsible', choices=APP_DEPT_CHOICES, required=False)
    root_cause = forms.ChoiceField(label='Root Cause', choices=ROOT_CAUSE_CHOICES, required=False)
    line = forms.ChoiceField(label='Line', choices=LINE_CHOICES, required=False)
    department = forms.ChoiceField(label='Department', choices=DEPARTMENT_CHOICES, required=False)    
    start_date = forms.DateField(label='Start Date', required=False)
    end_date = forms.DateField(label='End Date', required=False)
    shift = forms.ChoiceField(label='Shift', choices=SHIFT_CHOICES, required=False)
    start_tdate = forms.DateField(label='Start Transaction Date', required=False)   
    end_tdate = forms.DateField(label='End Transaction Date', required=False)   
    start_fdate = forms.DateField(label='Start Finalized Date', required=False)
    end_fdate = forms.DateField(label='End Finalized Date', required=False) 

class wtr_form(forms.Form):
    start_tdate = forms.DateField(label='Start Transaction Date', required=True)
    end_tdate = forms.DateField(label='End Transaction Date', required=True)

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'employee_name', 'badge_number', 'date', 'location',
            'item_number', 'work_order', 'item_description', 'supplier', 'non_conformances',
            'lead_supervisor', 'investigation_date', 'training', 'training_date',
            'counseling', 'counseling_date', 'disciplinary_action', 
            'disciplinary_action_date', 'notes', 'employee_signature',
            'employee_signature_date'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'investigation_date': forms.DateInput(attrs={'type': 'date'}),
            'training_date': forms.DateInput(attrs={'type': 'date'}),
            'counseling_date': forms.DateInput(attrs={'type': 'date'}),
            'disciplinary_action_date': forms.DateInput(attrs={'type': 'date'}),
            'employee_signature_date': forms.DateInput(attrs={'type': 'date'}),
        }
        #General Information
        employee_name = forms.CharField(label='Employee Name', required=True)
        badge_number = forms.CharField(label='Badge Number', required=False)
        date = forms.DateField(label='Date', required=True)
        location = forms.CharField(label='Location', required=True)
        item_number = forms.CharField(label='Item Number', required=False)
        work_order = forms.CharField(label='Work Order', required=False)
        item_description = forms.CharField(label='Item Description', required=False)
        #Supplier
        supplier = forms.ChoiceField(label='Supplier', choices=SUPPLIER_CHOICES, required=False)
        #Non Conformance(s)
        non_conformances = forms.MultipleChoiceField(label='Non Conformance(s)', required= True,
                                                     choices=Ticket.NON_CONFORMANCE_CHOICES,
                                                    widget=forms.CheckboxSelectMultiple)
        def clean_non_conformances(self):
            return ','.join(self.cleaned_data['non_conformances'])
        #Investigation
        lead_supervisor = forms.CharField(label='Lead Supervisor', required=False)
        investigation_date = forms.DateField(label='Investigation Date', required=False)
        #Corrective Action
        training = forms.BooleanField(label='Training', required=False)
        training_date = forms.DateField(label='Date', required=False)
        counseling = forms.BooleanField(label='Counseling', required=False)
        counseling_date = forms.DateField(label='Date', required=False)
        disciplinary_action = forms.BooleanField(label='Disciplinary Action', required=False)
        disciplinary_action_date = forms.DateField(label='Disciplinary Action Date', required=False)
        notes = forms.CharField(label='Notes', required=False)
        employee_signature = forms.CharField(label='Employee Signature', required=False)
        employee_signature_date = forms.DateField(label='Date', required=False)

class TicketReportForm(forms.Form):
    username = forms.CharField(label='Username', required=False)
    supervisor = forms.CharField(label='Supervisor', required=False)
    start_date = forms.DateField(label='Start Date', required=False)
    end_date = forms.DateField(label='End Date', required=False)

class rng_form(forms.Form):
    username = forms.CharField(label='Username', required=True)
    location_count = forms.IntegerField(label='Location Count', required=True)
    start_date = forms.DateField(label='Start Date', required=True)
    end_date = forms.DateField(label='End Date', required=True)
