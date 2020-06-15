from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Sum, Max, Count
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages

from user.models import Intake, Planning
from progression.models import Progress, CTRS
from .forms import ProgressForm, CTRSForm


class CTRSList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Intake
    template_name = 'danger_list.html'
    context_object_name = 'user_list'

    # def get_context_data(self, **kwargs):
    #     context = super(CTRSList, self).get_context_data(**kwargs)
    #     context['form'] = CTRSForm(initial={'post': self.object})
    #     context['user'] = Intake.objects.get(pk=self.kwargs.get('pk'))
    #     return context
    


class CTRSListDetail(FormMixin, DetailView):
    template_name = 're_danger.html'
    model = Intake
    form_class = CTRSForm
    context_object_name = 'user'
    queryset = Intake.objects.all()

    # DetailView와 FormView를 동시에 사용하기 위한 코드 추가
    def get_success_url(self):
        return reverse('danger_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(CTRSListDetail, self).get_context_data(**kwargs)
        context['form'] = CTRSForm(initial={'post': self.object})
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
        return super(CTRSListDetail, self).form_valid(form)


class ProgressList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Intake
    template_name = 'getplan_list.html'
    context_object_name = 'user_list'
    



class ProgressListDetail(FormMixin, DetailView):
    template_name = 're_getplan.html'
    model = Intake
    form_class = ProgressForm
    # context_object_name = 'user'
    # queryset = Intake.objects.all()

    # DetailView와 FormView를 동시에 사용하기 위한 코드 추가
    def get_success_url(self):
        return reverse('getplan_detail', kwargs={'pk': self.object.id})

    # 데이터 로딩
    def get_context_data(self, **kwargs):
        prog = Progress.objects.filter(CT_id=self.kwargs.get('pk')).aggregate(a1_c=Sum('inmedical_A1_C_1'),a2_c=Sum('inmedical_A2_C_1'),
        a3_c=Sum('inmedical_A3_C_1'),a4_c=Sum('inmedical_A4_C_1'), a1=Sum('inmedical_A1_YN_1'),a2=Sum('inmedical_A2_YN_1'), 
        a3=Sum('inmedical_A3_YN_1'), a4=Sum('inmedical_A4_YN_1'),
        # sum 임시방편임
        med_a_1=Sum('inmedical_A_1_sum'),
        med_a_2=Sum('inmedical_A_2_sum'),
        med_a_3=Sum('inmedical_A_3_sum'),
        med_a_4=Sum('inmedical_A_4_sum'),
        med_b=Sum('inmedical_B_sum'),
        med_c=Sum('inmedical_C_sum'),
        med_d=Sum('inmedical_D_sum'),
        med_e=Sum('inmedical_E_sum'),
        med_f=Sum('inmedical_F_sum'),
        med_g=Sum('inmedical_G_sum'),
        men_a=Sum('inmental_A_sum'),
        men_b=Sum('inmental_B_sum'),
        men_c=Sum('inmental_C_sum'),
        case_a=Sum('incase_A_sum'),
        case_b=Sum('incase_B_sum'),
        case_c=Sum('incase_C_sum'),
        inmedical_B1_YN=Sum('inmedical_B1_YN'),
        inmedical_B2_YN=Sum('inmedical_B2_YN'),
        inmedical_B3_YN=Sum('inmedical_B3_YN'),
        inmedical_C1_YN=Sum('inmedical_C1_YN'),
        inmedical_C2_YN=Sum('inmedical_C2_YN'),
        inmedical_C3_YN=Sum('inmedical_C3_YN'),
        inmedical_D1_YN=Sum('inmedical_D1_YN'),
        inmedical_D2_YN=Sum('inmedical_D2_YN'),
        inmedical_D3_YN=Sum('inmedical_D3_YN'),
        inmedical_E1_YN=Sum('inmedical_E1_YN'),
        inmedical_E2_YN=Sum('inmedical_E2_YN'),
        inmedical_F1_YN=Sum('inmedical_F1_YN'),
        inmedical_F2_YN=Sum('inmedical_F2_YN'),
        inmedical_F3_YN=Sum('inmedical_F3_YN'),
        inmedical_G1_YN=Sum('inmedical_G1_YN'),
        inmedical_G2_YN=Sum('inmedical_G2_YN'),
        inmedical_G3_YN=Sum('inmedical_G3_YN'),
        # cost
        med_a_cost_1=Sum('inmedical_A_1_cost'),
        med_a_cost_2=Sum('inmedical_A_2_cost'),
        med_a_cost_3=Sum('inmedical_A_3_cost'),
        med_a_cost_4=Sum('inmedical_A_4_cost'),
        med_b_cost=Sum('inmedical_B_cost'),
        med_c_cost=Sum('inmedical_C_cost'),
        med_d_cost=Sum('inmedical_D_cost'),
        med_e_cost=Sum('inmedical_E_cost'),
        med_f_cost=Sum('inmedical_F_cost'),
        med_g_cost=Sum('inmedical_G_cost'),
        men_a_cost=Sum('inmental_A_cost'),
        men_b_cost=Sum('inmental_B_cost'),
        men_c_cost=Sum('inmental_C_cost'),
        case_a_cost=Sum('incase_A_cost'),
        case_b_cost=Sum('incase_B_cost'),
        case_c_cost=Sum('incase_C_cost')
        )
        ctrs1 = CTRS.objects.filter(CT_id=self.kwargs.get('pk')).filter(danger_label='1차').aggregate(label_1=Sum('total'))
        ctrs2 = CTRS.objects.filter(CT_id=self.kwargs.get('pk')).filter(danger_label='2차').aggregate(label_2=Sum('total'))
        ctrs3 = CTRS.objects.filter(CT_id=self.kwargs.get('pk')).filter(danger_label='3차').aggregate(label_3=Sum('total'))
        date1 = CTRS.objects.filter(CT_id=self.kwargs.get('pk')).filter(danger_label='1차').last()
        date2 = CTRS.objects.filter(CT_id=self.kwargs.get('pk')).filter(danger_label='2차').last()
        date3 = CTRS.objects.filter(CT_id=self.kwargs.get('pk')).filter(danger_label='3차').last()

        context = super(ProgressListDetail, self).get_context_data(**kwargs)
        context['form'] = ProgressForm(initial={'post': self.object})
        # context['intake'] = Intake.objects.all()
        # context['user'] = Intake.objects.get(Name=self.object.pk)
        context['user'] = Intake.objects.get(pk=self.kwargs.get('pk'))
        # 계획 DB loading
        # context['planning'] = Planning.objects.get(setplan_name=self.kwargs.get('Name'))
        context['planning'] = Planning.objects.get(CT_id=self.kwargs.get('pk'))
        # 위기분류 DB loading
        context['ctrs1'] = ctrs1
        context['ctrs2'] = ctrs2
        context['ctrs3'] = ctrs3
        context['date1'] = date1
        context['date2'] = date2
        context['date3'] = date3
        # 진행 DB loading
        # columns = Progress.objects.filter(CT_id=self.kwargs.get('pk')).values()
        # context['progress'] = Progress.objects.get(pk=self.kwargs.get('pk'))
        context['progress'] = prog
        context['progress_text'] = Progress.objects.filter(CT_id=self.kwargs.get('pk'))
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
        return super(ProgressListDetail, self).form_valid(form)



class UpdateListView(TemplateView):
    template_name = 'update_list.html'

    def get(self, request, *args, **kwargs):
        print(request.GET)
        queryset = Progress.objects.all()
        ctx = {
            'update_list': queryset
        }
        return self.render_to_response(ctx)


class UpdateDetailView(TemplateView):
    template_name = 'update_detail.html'
    queryset = Progress.objects.all()
    pk_url_kwargs = 'progress_id'

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        article = queryset.filter(pk=pk).first()

        if not article:
            raise Http404('invalid pk')
        return article

    def get(self, request, *args, **kwargs):
        prog = self.get_object()

        ctx = {
            'getplan': prog
        }
        return self.render_to_response(ctx)


class ArticleCreateUpdateView(LoginRequiredMixin, TemplateView):
    # login_url = settings.LOGIN_URL
    template_name = 'progress_update.html'
    queryset = Progress.objects.all()
    pk_url_kwargs = 'progress_id'

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        prog = queryset.filter(pk=pk).first()

        if pk:
          if not prog:
            raise Http404('invalid pk')
        #   elif prog.author != self.request.user:                             # 작성자가 수정하려는 사용자와 다른 경우
        #     raise Http404('invalid user')
        return prog

    def get(self, request, *args, **kwargs):
        prog = self.get_object()

        ctx = {
            'prog': prog,
        }
        return self.render_to_response(ctx)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        post_data = {key: request.POST.get(key) for key in ()} # 작성자를 입력받지 않도록 수정
        for key in post_data:
            if not post_data[key]:
                messages.error(self.request, '{} 값이 존재하지 않습니다.'.format(key), extra_tags='danger')

        # post_data['author'] = self.request.user                                  # 작성자를 현재 사용자로 설정

        if len(messages.get_messages(request)) == 0:
            if action == 'create':
                prog = Progress.objects.create(**post_data)
                messages.success(self.request, '입력 내용이 저장되었습니다.')
            elif action == 'update':
                prog = self.get_object()
                for key, value in post_data.items():
                    setattr(prog, key, value)
                prog.save()
                messages.success(self.request, '입력 내용이 저장되었습니다.')
            else:
                messages.error(self.request, '알 수 없는 요청입니다.', extra_tags='danger')

            return HttpResponseRedirect('/update/')

        ctx = {
            'prog': self.get_object() if action == 'update' else None
        }
        return self.render_to_response(ctx)