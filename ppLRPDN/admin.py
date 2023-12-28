from django.contrib import admin
from .models import NewPickingProblem, Ticket, ActionLog
# Register your models here.

@admin.register(NewPickingProblem)
class NewPickingProblemAdmin(admin.ModelAdmin):
    list_display = ('reference_number', 'status', 'name', 'date', 'time', 'work_order', 'job_number', 'part_number', 
                    'item_dsc', 'defect', 'total_count', 'total_affected', 'unit_type', 
                    'department', 'app_dept', 'line', 'comment','employee_username', 'location', 
                    'transaction_date', 'transaction_time', 'applied', 'root_cause', 'final_reason',
                    'final_comments', 'finalized', 'finalized_username', 'finalized_date', 'finalized_time')
    list_filter = ('date', 'app_dept')
    search_fields = ('name', 'date', 'time', 'work_order')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'employee_name', 'badge_number', 'date', 
                    'location', 'item_number', 'work_order', 'item_description', 
                    'supplier', 'non_conformances', 'lead_supervisor', 'investigation_date', 
                    'training', 'training_date', 'counseling', 'counseling_date', 
                    'disciplinary_action', 'disciplinary_action_date', 'notes', 
                    'employee_signature', 'employee_signature_date')
    list_filter = ('date', 'location')
    search_fields = ('employee_name', 'badge_number', 'date', 'location', 'item_number', 'work_order')
 
@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    list_display = ('action_type', 'user', 'reference_number', 'timestamp')
    list_filter = ( 'action_type', 'user')
    search_fields = ('action_type', 'user', 'reference_number', 'timestamp')