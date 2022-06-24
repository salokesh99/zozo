from pyexpat import model
# from tkinter import SE
# from wsgiref.util import shift_path_info
from django.db import models



class User(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=18)
    employee_id = models.CharField(unique=True, max_length=18)
    country_code = models.CharField( max_length=3)
    mobile_number = models.CharField( max_length=13)
    email_id = models.EmailField(unique=True, max_length=75)
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30) 
    department =  models.ForeignKey('Department', null=True, on_delete=models.SET_NULL)
    date_of_joining = models.DateTimeField()
    last_working_day = models.DateTimeField(null=True)
    shift = models.ForeignKey('Shift',null=True, on_delete=models.SET_NULL)
    role = models.ForeignKey('Role', null=True, on_delete=models.SET_NULL)
    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_edited = models.BooleanField(default=False)


class Ticket(models.Model):

    uuid = models.CharField(max_length=90)
    manual_id = models.IntegerField()
    title = models.CharField( max_length=200)
    description = models.TextField(max_length=3000)
    attachments = models.ForeignKey('Attachment', null=True, on_delete=models.SET_NULL )
    status = models.ForeignKey('Status', null=True, on_delete=models.SET_NULL)
    reported_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='tickets_reported')
    assigned_to = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,  related_name='tickets_assigned',)
    reporter_department = models.ForeignKey('Department', null=True, on_delete=models.SET_NULL, related_name='reported_issues')
    assignee_department = models.ForeignKey('Department', null=True, on_delete=models.SET_NULL, related_name='assigned_issues')
    help_topics = models.ForeignKey('HelpTopic', null=True, on_delete=models.SET_NULL)
    # tags = 'multiple individual words'
    severity = models.ForeignKey('Severity', null=True, on_delete=models.SET_NULL)
    priority = models.ForeignKey('Priority', null=True, on_delete=models.SET_NULL)


class Attachment(models.Model):
    name = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    file_type = models.CharField(max_length=128)
    file_path = models.CharField(max_length=128)
    is_edited = models.BooleanField(default=False)

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class Department(models.Model):
    name = models.CharField(max_length=128)
    size = models.CharField(null=True,max_length=128)
    address = models.CharField(null=True, max_length=128)
    contact_person = models.CharField(max_length=128)
    country_code = models.CharField( max_length=3)
    contact_number = models.CharField( max_length=13)
    email_id = models.EmailField(unique=True, max_length=75)
    manager = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='manager')
    manager_email_id = models.EmailField(unique=True, max_length=75)
    Manager_contact = models.IntegerField(null=True)
    manager_country_code = models.CharField(null=True, max_length=3)
    members = models.ManyToManyField(User, related_name='departments')

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = self.objects.all().aggregate(largest=models.Max('manual_id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.manual_id = last_id + 1

        super(Ticket, self).save(*args, **kwargs)


class Comment(models.Model):
    # title = models.CharField(max_length=75)
    description = models.TextField(null=True, max_length=2000)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    attachments = models.FileField(null=True,upload_to ='uploads/')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class Templates(models.Model):
    title = models.CharField(null=True, max_length=75)
    description = models.TextField(null=True, max_length=200)
    department = models.ForeignKey('Department', null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    last_used_at = models.DateTimeField(auto_now_add=True)

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

class HelpTopic(models.Model):
    title = models.CharField(null=True, max_length=75)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey('Department',  null=True, on_delete=models.SET_NULL)

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class Shift(models.Model):
    title = models.CharField(max_length=75)
    start_time = models.TimeField()
    end_time = models.TimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='current_shift')

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

class Role(models.Model):
    title = models.CharField(max_length=75)
    pub_date = models.DateTimeField(null=True,)
    author = models.ForeignKey(User, null=True, related_name='user_role', on_delete=models.SET_NULL)

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class Priority(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class Severity(models.Model):
    title = models.CharField(max_length=20)
    # pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class Status(models.Model):
    title = models.CharField(max_length=30)
    # pub_date = models.DateTimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)




# Tags to be introduced.








# ++++++++++++++++++++++ draft ++++++++++++++++++++++++++++#
# class Department(models.Model):

#     name = models.CharField(max_length=128)
#     email_id = models.EmailField(max_length=75)
#     mobile_number = models.CharField(max_length=13)
#     description = models.CharField(max_length=200)
#     #manager to be presented in Name and email format only.
#     manager = models.ForeignKey(Users)
#     members = models.ManyToManyField(
#         Users,
#         through='Membership',
#         through_fields=('group', 'person'),
#     )

#     # Regular Fields
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     is_archive = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

    # Rest of your model data


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, max_length=255)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     author = models.TextField()


# class Comment(models.Model):
#     name = models.CharField(max_length=42)
#     email = models.EmailField(max_length=75)
#     website = models.URLField(max_length=200, null=True, blank=True)
#     content = models.TextField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)


# class Employee(models.Model):  
#     first_name = models.CharField(max_length=30)  
#     last_name = models.CharField(max_length=30) 

# class Musician(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     instrument = models.CharField(max_length=200)

# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()


# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     def __str__(self):
#         return self.name
        
# class Citizenship(models.Model):
#     person = models.OneToOneKey(Person, on_delete=models.CASCADE)
#     country = models.CharField(max_length=30)


# class Customer(models.Model):
#     name = models.CharField(max_length=30)
#     def __str__(self):
#         return self.name
        
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order_details = models.TextField()


# class Person(models.Model):
#     name = models.CharField(max_length=30)

# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(
#         Person,
#         through='Membership',
#         through_fields=('group', 'person'),
#     )

# class Membership(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     inviter = models.ForeignKey(
#         Person,
#         on_delete=models.CASCADE,
#         related_name="membership_invites",
#     )
#     invite_reason = models.CharField(max_length=64)
    