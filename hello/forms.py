from django import forms  
from hello.models import *


class UserForm(forms.ModelForm):  

    class Meta:  
        model = User  
        fields = "__all__" 
 

class TicketForm(forms.ModelForm):  

    class Meta:  
        model = Ticket  
        fields = "__all__" 
 

class AttachmentForm(forms.ModelForm):  

    class Meta:  
        model = Attachment  
        fields = "__all__" 
 

class DepartmentForm(forms.ModelForm):  

    class Meta:  
        model = Department  
        fields = "__all__" 
 

class CommentForm(forms.ModelForm):  

    class Meta:  
        model = Comment  
        fields = "__all__" 
 

class TemplateForm(forms.ModelForm):  

    class Meta:  
        model = Template 
        fields = "__all__" 
 

class HelptopicForm(forms.ModelForm):  

    class Meta:  
        model = HelpTopic  
        fields = "__all__" 
 

class ShiftForm(forms.ModelForm):  

    class Meta:  
        model = Shift  
        fields = "__all__" 
 

class RoleForm(forms.ModelForm):  

    class Meta:  
        model = Role  
        fields = "__all__" 
 

class StatusForm(forms.ModelForm):  

    class Meta:  
        model = Status  
        fields = "__all__" 
 

class SeverityForm(forms.ModelForm):  

    class Meta:  
        model = Severity  
        fields = "__all__" 
 

class PriorityForm(forms.ModelForm):  

    class Meta:  
        model = Priority  
        fields = "__all__" 
 
