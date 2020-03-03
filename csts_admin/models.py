from django.db import models
from djongo.models import EmbeddedModelField, ArrayModelField

# Create your models here.
class Login(models.Model):
    types = (
        ('Admin', 'Admin'),
        ('Client', 'Client'),
        ('Agent', 'Agent')
    )
    user_type = models.CharField(max_length=100 , choices=types)
    username = models.CharField(max_length=100 , unique=True , null=False , blank=False)
    password = models.CharField(max_length=25 , null=False , blank=False)


class Address(models.Model):
    """Embedded model to store address of user"""
    types = (
        ('Admin', 'Admin'),
        ('Client', 'Client'),
        ('Agent', 'Agent')
    )
    user_type = models.CharField(max_length=100 , choices=types)
    add_line1 = models.CharField(max_length=255, blank=False, null=False)
    add_line2 = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(max_length=255, blank=False, null=False)
    zip_code = models.IntegerField(blank=False, null=False)


class Client(models.Model):
    insurance = (
        ('Health' , 'Health'),
        ('Business' , 'Business'),
        ('Visitors' , 'Visitors'),
        ('Compliance' , 'Compliance')
    )

    client_status = (
        ('Active' , 'Active'),
        ('Inactive' , 'Inactive')
    )
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True) 
    phone = models.CharField(max_length=10, blank=False, null=False)
    address = EmbeddedModelField(model_container=Address)
    insurance_type = models.CharField(max_length=255 , choices=insurance)
    referred_by = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255 , choices=client_status , default="Active")

class Agent(models.Model):
    agent_status = (
        ('Online' , 'Online'),
        ('Offline' , 'Offline'),
        ('Assigned' , 'Assigned')
    )
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True) 
    phone = models.CharField(max_length=10, blank=False, null=False)
    address = EmbeddedModelField(model_container=Address)
    status = models.CharField(max_length=255 , choices=agent_status , default="Online")

class CstsAdmin(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True) 
    phone = models.CharField(max_length=10, blank=False, null=False)
    address = EmbeddedModelField(model_container=Address)

class ClientComments(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True, null=True)

class AgentComments(models.Model):
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True, null=True)

class Ticket(models.Model):
    ticket_status = (
        ('Pending' , 'Pending'),
        ('Active' , 'Active'),
        ('Completed' , 'Completed')
    )
    priority = (
        ('Low' , 'Low'),
        ('Medium' , 'Medium'),
        ('High' , 'High')
    )
    title = models.CharField(max_length=255, blank=False, null=False)
    client_comments = ArrayModelField(model_container = ClientComments)
    agent_comments = ArrayModelField(model_container = AgentComments)
    status = models.CharField(max_length=255 , choices=ticket_status , default="Pending")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    assigned_to = models.ForeignKey(Agent, on_delete=models.CASCADE)
    active_status = models.DateTimeField(auto_now=True)
    completed_status = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=255 , choices=priority , default="Medium")

class Feedback(models.Model):
    user_email = models.CharField(max_length=255, blank=False, null=False)
    ratings = models.IntegerField(blank=False, null=False , default=1)
    reviews = models.CharField(max_length=255, blank=False, null=False)
    agent_username = models.CharField(max_length=255, blank=False, null=False)






