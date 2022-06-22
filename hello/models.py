from pyexpat import model
from wsgiref.util import shift_path_info
from django.db import models



class Users(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=18)
    employee_id = models.CharField(unique=True, max_length=18)
    mobile_number = models.CharField(max_length=13)
    email_id = models.EmailField(unique=True, max_length=75)
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30) 
    department =  models.ForeignKey('Department')
    date_of_joining = models.DateTimeField()
    last_working_day = models.DateTimeField()
    # shift = 'options_field'
    # role = 'options field'

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)



class Department(models.Model):

    name = models.CharField(max_length=128)
    email_id = models.EmailField(max_length=75)
    mobile_number = models.CharField(max_length=13)
    description = models.CharField(max_length=200)
    #manager to be presented in Name and email format only.
    manager = models.ForeignKey(Users)
    members = models.ManyToManyField(
        Users,
        through='Membership',
        through_fields=('group', 'person'),
    )


    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

class Tickets(models.Model):

    uuid = models.AutoField()
    manual_id = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    # attachments = 
    # status = 'optional_field'
    #  to be presented in Name and email format only
    reported_by = models.ForeignKey(Users)
    assigned_to = models.ForeignKey(Users)
    reporter_department = models.ForeignKey(Department)
    assignee_department = models.ForeignKey(Department)
    # help_topics = 'to be decided from a pool of options of help topics 
    # tags = 'multiple individual words'
    # severity = 'to be chosen from severity options'
    # priority = 'to be chosen from priority options'


class Attachment():








    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)










    # Rest of your model data

    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = self.objects.all().aggregate(largest=models.Max('manual_id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.manual_id = last_id + 1

        super(Tickets, self).save(*args, **kwargs)


















class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30) 

class Musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    instrument = models.CharField(max_length=200)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Person(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
        
class Citizenship(models.Model):
    person = models.OneToOneKey(Person, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)


class Customer(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
        
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_details = models.TextField()


class Person(models.Model):
    name = models.CharField(max_length=30)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)
    