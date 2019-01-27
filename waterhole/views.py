from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ComitteRegistrationForm

# Create your views here.
class ComitteView(View):
    @method_decorator(login_required)
    def get(self,request):
        template_name = 'comitte.html'
        user = request.user
        admin_profile = user.get_adminwaterhole_profile()
        waterhole = admin_profile.waterhole_admin
        comitte = waterhole.waterhole_comitte
        form = ComitteRegistrationForm(instance = comitte)
        context = {
            "comittte":"active",
            'form':form,
            'comitte':comitte,
        }
        return render(request,template_name,context)
    def post(self,request):
        template_name ='comitte.html'
        user = request.user
        admin_profile = user.get_adminwaterhole_profile()
        waterhole = admin_profile.waterhole_admin
        comitte = waterhole.waterhole_comitte
        form = ComitteRegistrationForm(instance = comitte, data=request.POST)
        print(waterhole)
        if form.is_valid():
            new_comite = form.save(commit = False)
            new_comite.waterhole_comitte = waterhole
            new_comite.save()
            messages.success(self.request, 'datos guardados satisfactoriamente.')
            return redirect('waterhole:comitte')
        else:
            form = ComitteRegistrationForm(instance = comitte)
            context = {
                "comittte":"active",
                'form':form,
                'comitte':comitte,
            }
            return render(request,template_name,context)

    
    