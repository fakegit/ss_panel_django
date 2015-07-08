from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.http import HttpResponse
from django.template import RequestContext
from .forms import AdminLoginForm
from django.views.decorators.csrf import csrf_exempt
from utils.encrptyutils import EncrptyUtils


def index(request):
    form = AdminLoginForm()
    return render_to_response('adminmgr/admin_login.html',{'form':form})
    
@csrf_exempt
def adminLoginForm(request):
    adminLoginForm = AdminLoginForm(request.POST)
    if adminLoginForm.is_valid():
        adminusername = adminLoginForm.cleaned_data['adminusername']
        adminuserpwd = adminLoginForm.cleaned_data['adminuserpwd']
        if adminusername =='admin' and adminuserpwd == EncrptyUtils.getMd5('123qwe'):
            return render_to_response('adminmgr/admin_front.html')

    else:
        return render_to_response('adminmgr/admin_login.html',{'form':adminLoginForm})


def nodeEdit(request):


    return render_to_response('adminmgr/admin_front_node.html')

def userMgr(request):

    return render_to_response('adminmgr/admin_front_usermgr.html')


def adminLogout(request):

    form = AdminLoginForm()

    return render_to_response('adminmgr/admin_login.html',{'form':form})
    
