from urllib import request
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
# from django.views.generic import ListView
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from .models import *
from .forms import *
from django.shortcuts import render, redirect  





def home(request):
    return HttpResponse("Hello, Django!")

# def hello_there(request, name):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)


def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def zozo_home(request):
    d= {
        'name' : 'Lokesh',
        'Team' : 'PSI',
        'batch_name' : 'batch - 11' 
    }
    return HttpResponse(d.items())



class UserView():
    # model = User
    # template_name = 'users/user.html'
    # context_object_name = 'users'

    def UserListView(request):
        user_list = User.objects.filter(is_active=True)
        # user_list = ['shyam', 'ram', 'udham', 'dushyant', 'Lokesh']
        # return HttpResponse(user_list)
        return render(request,"hello/list.html",{'user_list':user_list})  
    
    def UserDetailView( request, id):
        user_detail =User.objects.filter(is_active=True, id=id)

        return user_detail


    def UserCreateView( request):
        user_form = UserForm(request.POST)
        if user_form.is_valild():
            try:
                form.save()
                return redirect('/details')
            except:
                pass
        else:
            form = UserForm() 
        return  render((request,'index.html',{'form':form}))



    def UserEditView( request, id):
        user = User.objects.get(id=id)  
        return render(request,'edit.html', {'Users':user}) 

            
    def UserUpdateView( request, id):  
        user = User.objects.get(id=id)  
        form = UserForm(request.POST, instance = user)  
        if form.is_valid():  
            form.save()  
            return redirect("/details")  
        return render(request, 'edit.html', {'user': user})  


    def UserDeleteView(self, request, id):  
        user = User.objects.get(id=id)  
        user.is_active = False
        user.save()
        return redirect("/details")  







#         def emp(request):  
#     if request.method == "POST":  
#         form = EmployeeForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect('/show')  
#             except:  
#                 pass  
#     else:  
#         form = EmployeeForm()  
#     return render(request,'index.html',{'form':form})  


        









# # UserUpdateView
# # UserDeleteView







# #         UserListView
# # ,     UserDetailView
# #       UserCreateView
# # ',    UserUpdateView
# # ',    UserDeleteView
# #       TicketListView
# # ',  TicketDetailView
# #     TicketCreateView
# # /', TicketUpdateView
# # /', TicketDeleteView
# #   AttachmentListView
# # AttachmentDetailView
# # AttachmentCreateView
# # AttachmentUpdateView
# # AttachmentDeleteView
# #   DepartmentListView
# # DepartmentDetailView
# # DepartmentCreateView
# # DepartmentUpdateView
# # DepartmentDeleteView
# #      CommentListView
# # ,  CommentDetailView
# #    CommentCreateView
# # ', CommentUpdateView
# # ', CommentDeleteView
# #     TemplateListView
# #   TemplateDetailView
# #   TemplateCreateView
# # , TemplateUpdateView
# # , TemplateDeleteView
# #    HelpTopicListView
# #  HelpTopicDetailView
# #  HelpTopicCreateView
# #  HelpTopicUpdateView
# #  HelpTopicDeleteView
# #        ShiftListView
# # l',  ShiftDetailView
# #      ShiftCreateView
# # e/', ShiftUpdateView
# # e/', ShiftDeleteView
# #         RoleListView
# # il',  RoleDetailView
# #       RoleCreateView
# # te/', RoleUpdateView
# # te/', RoleDeleteView
# #       StatusListView
# # ',  StatusDetailView
# #     StatusCreateView
# # /', StatusUpdateView
# # /', StatusDeleteView
# #     SeverityListView
# #   SeverityDetailView
# #   SeverityCreateView
# # , SeverityUpdateView
# # , SeverityDeleteView
# #     PriorityListView
# #   PriorityDetailView
# #   PriorityCreateView
# # , PriorityUpdateView
# # , PriorityDeleteView