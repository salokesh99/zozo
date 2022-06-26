from pyexpat import model
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
    date_of_joining = models.DateTimeField(null=True)
    last_working_day = models.DateTimeField(null=True)
    shift = models.ForeignKey('Shift',null=True, on_delete=models.SET_NULL)
    role = models.ForeignKey('Role', null=True, on_delete=models.SET_NULL)
    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_edited = models.BooleanField(default=False)

    class Meta:  
        db_table = "user"  
    
    def __str__(self):
        return self.username


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
    # Regular Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    class Meta:  
        db_table = "ticket"
    
    def __str__(self):
        return self.manual_id

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

    class Meta:  
        db_table = "attachment"
    
    def __str__(self):
        return self.name

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

    class Meta:  
        db_table = "department"  

    def __str__(self):
        return self.name

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

    class Meta:  
        db_table = "comment"  


class Template(models.Model):

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

    class Meta:  
        db_table = "templates"  


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

    class Meta:  
        db_table = "helptopic"  

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

    class Meta:  
        db_table = "shift"  

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

    class Meta:  
        db_table = "role"  


# https://docs.djangoproject.com/en/4.0/ref/models/fields/
# https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django
class Status(models.Model):

    NEW = 'NEW'
    ONGOING = 'ONG'
    PENDING = 'PEN'
    WAITING = 'WIT'
    SNOOZE = 'SNZ'
    BLOCKED = 'BLK'
    RESOLVED = 'RES'
    CLOSED = 'CLS'
    DUPLICATE = 'DPL'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (ONGOING, 'Ongoing'),
        (PENDING, 'Pending'),
        (WAITING, 'Waiting'),
        (SNOOZE, 'Snooze'),
        (BLOCKED, 'Blocked'),
        (RESOLVED, 'Resolved'),
        (CLOSED, 'Closed'),
        (DUPLICATE, 'Duplicate')
    ]

    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=NEW 
    )

    class Meta:  
        db_table = "status"  


class Severity(models.Model):

    S1 = 'S1'
    S2 = 'S2'
    S3 = 'S3'
    S4 = 'S4'

    SEVERITY = [
        (S1, 'S1'),
        (S2, 'S2'),
        (S3, 'S3'),
        (S4, 'S4')
    ]

    severity = models.CharField(
        max_length=2,
        choices=SEVERITY,
        default=S1 
    )

    class Meta:  
        db_table = "severity"  


class Priority(models.Model):

    P1 = 'P0'
    P2 = 'P1'
    P3 = 'P2'
    P4 = 'P3'

    PRIORITY = [
        (P1, 'P0'),
        (P2, 'P1'),
        (P3, 'P2'),
        (P4, 'P3')
    ]

    priority = models.CharField(
        max_length=2,
        choices=PRIORITY,
        default=P1
    )

    class Meta:  
        db_table = "priority"  



################################################################################
###############################################################################
# helpful in dev

# class Priority(models.Model):
#     title = models.CharField(max_length=20)
#     pub_date = models.DateTimeField()
#     author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

#     # Regular Fields
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     is_edited = models.BooleanField(default=False)
#     is_archive = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)


# class Severity(models.Model):
#     title = models.CharField(max_length=20)
#     # pub_date = models.DateTimeField('date published')
#     author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

#     # Regular Fields
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     is_edited = models.BooleanField(default=False)
#     is_archive = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)


# class Status(models.Model):
#     title = models.CharField(max_length=30)
#     # pub_date = models.DateTimeField()
#     author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

#     # Regular Fields
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     is_edited = models.BooleanField(default=False)
#     is_archive = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

# class Status(models.TextChoices):
#     UNSTARTED = 'u', "Not started yet"
#     ONGOING = 'o', "Ongoing"
#     FINISHED = 'f', "Finished"
#     Created = 'Created'

# class YearInSchool(models.TextChoices):
#     FRESHMAN = 'FR', 'Freshman'
#     SOPHOMORE = 'SO', 'Sophomore'
#     JUNIOR = 'JR', 'Junior'
#     SENIOR = 'SR', 'Senior'
#     GRADUATE = 'GR', 'Graduate'

#     year_in_school = models.CharField(
#         max_length=2,
#         choices=YearInSchool.choices,
#         default=YearInSchool.SOPHOMORE,
#     )


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
    



# (username='loke@123',
# password='welcome@123',
# employee_id='SSN0123',
# country_code = '+91',
# mobile_number = '8050408646',
# email_id = 'salokesh99@gmail.com',
# first_name = 'lokesh',
# last_name = 'ajja' )