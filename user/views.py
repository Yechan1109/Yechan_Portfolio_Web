from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import FormView, FormMixin
from django.views.generic import ListView, DetailView
from counselor.forms import UserRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.views import LoginView

from .models import Intake, Program, Planning
from user.forms import IntakeForm, PlanningForm, ProgramForm, UploadFileForm

from django.http import HttpResponseRedirect

class UserLoginIndexView(LoginView):
    authentication_form = LoginForm
    template_name = 're_index.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)


def main(request):
    return render(request, 're_main.html')


class IntakeView(LoginRequiredMixin, FormView):
    login_url = '/login'
    
    template_name = 're_initial.html'
    form_class = IntakeForm
    success_url = '/main/'

    # def form_valid(self, form):
    #     form.save()
    #     return super(IntakeView, self).form_valid(form)

class PlanningList(LoginRequiredMixin, ListView):
    login_url = "/login"
    model = Intake
    template_name = 'setplan_list.html'
    context_object_name = 'user_list'


class PlanningListDetail(LoginRequiredMixin, FormMixin, DetailView):
    login_url = "/login"
    template_name = 're_setplan.html'
    model = Intake
    form_class = PlanningForm
    context_object_name = 'user'
    queryset = Intake.objects.all()

    # DetailView와 FormView를 동시에 사용하기 위한 코드 추가
    def get_success_url(self):
        return reverse('setplan_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PlanningListDetail, self).get_context_data(**kwargs)
        context['form'] = PlanningForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PlanningListDetail, self).form_valid(form)


# class PlanningView(FormView):
#     template_name = 're_setplan.html'
#     form_class = PlanningForm
#     success_url = '/main/'
# if action == 'create':
#                 prog = Progress.objects.create(**post_data)
#                 messages.success(self.request, '입력 내용이 저장되었습니다.')

class ProgramView(LoginRequiredMixin, FormView):
    login_url = "/login"
    template_name = 're_perfor.html'
    form_class = ProgramForm
    success_url = '/perfor'

    # def get_success_url(self):
    #     return reverse('perfor', kwargs={'pk': self.object.id})

    def get_context_data(self):
        program = Program.objects.all()
        context = {
            'programs': program,
        }
        return context


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        messages.success(request, '입력 내용이 저장되었습니다.')

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/upload')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})