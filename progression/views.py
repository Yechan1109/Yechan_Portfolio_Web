from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Sum, Max, Count
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages

from django.views.generic.edit import UpdateView

from user.models import Intake, Planning, Program
from progression.models import Progress, CTRS
from .forms import ProgressForm, CTRSForm
from .forms import UpdateForm
# for PDF
# from user.render import Render
# from django.views.generic import View

class CTRSList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Intake
    template_name = 'danger_list.html'
    context_object_name = 'user_list'

    # def get_context_data(self, **kwargs):
    #     context = super(CTRSList, self).get_context_data(**kwargs)
    #     context['user_list'] = Intake.objects.filter(id=self.kwargs.get('pk'))
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
    queryset = Intake.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProgressList, self).get_context_data(**kwargs)
        context['setplan_list'] = Planning.objects.all()
        return context



class ProgressListDetail(FormMixin, DetailView):
    template_name = 're_getplan.html'
    model = Intake
    form_class = ProgressForm
    # context_object_name = 'user'
    # queryset = Intake.objects.all()

    # DetailView와 FormView를 동시에 사용하기 위한 코드 추가
    # def get_success_url(self):
    #     return reverse('getplan_detail', kwargs={'pk': self.object.id})


    # 데이터 로딩
    def get_context_data(self, **kwargs):
        prog = Progress.objects.filter(CT_id=self.kwargs.get('pk')).aggregate(a1_c=Sum('inmedical_A1_C_1'),a2_c=Sum('inmedical_A2_C_1'),
        a3_c=Sum('inmedical_A3_C_1'),a4_c=Sum('inmedical_A4_C_1'),
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
        med_a_cost=Sum('inmedical_A_cost'),
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
        if prog['med_a_cost'] is None:prog['med_a_cost']=0
        if prog['med_b_cost'] is None:prog['med_b_cost']=0
        if prog['med_c_cost'] is None:prog['med_c_cost']=0
        if prog['med_d_cost'] is None:prog['med_d_cost']=0
        if prog['med_e_cost'] is None:prog['med_e_cost']=0
        if prog['med_f_cost'] is None:prog['med_f_cost']=0
        if prog['med_g_cost'] is None:prog['med_g_cost']=0

        if prog['men_a_cost'] is None:prog['men_a_cost']=0
        if prog['men_b_cost'] is None:prog['men_b_cost']=0
        if prog['men_c_cost'] is None:prog['men_c_cost']=0

        if prog['case_a_cost'] is None:prog['case_a_cost']=0
        if prog['case_b_cost'] is None:prog['case_b_cost']=0
        if prog['case_c_cost'] is None:prog['case_c_cost']=0
        total_cost = prog['med_a_cost'] + prog['med_b_cost'] + prog['med_c_cost'] + prog['med_d_cost'] + prog['med_e_cost'] + prog['med_f_cost'] \
        + prog['med_g_cost'] + prog['men_a_cost'] + prog['men_b_cost'] + prog['men_c_cost'] + prog['case_a_cost'] + prog['case_b_cost'] + prog['case_c_cost']
        ctrs1 = CTRS.objects.filter(CT_id=self.kwargs.get('pk')).filter(danger_label='1차').aggregate(L1=Sum('sum_1'),L2=Sum('sum_2'),L3=Sum('sum_3'),L4=Sum('sum_4'), L5=Sum('total'))
        ctrs2 = CTRS.objects.filter(CT_id=self.kwargs.get('pk')).filter(danger_label='2차').aggregate(L1=Sum('sum_1'),L2=Sum('sum_2'),L3=Sum('sum_3'),L4=Sum('sum_4'), L5=Sum('total'))
        ctrs3 = CTRS.objects.filter(CT_id=self.kwargs.get('pk')).filter(danger_label='3차').aggregate(L1=Sum('sum_1'),L2=Sum('sum_2'),L3=Sum('sum_3'),L4=Sum('sum_4'), L5=Sum('total'))
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
        try:
            context['planning'] = Planning.objects.get(CT_id=self.kwargs.get('pk'))
        except Planning.DoesNotExist:
            raise Http404("지원계획이 존재하지 않습니다")
        # 위기분류 DB loading
        context['ctrs1'] = ctrs1
        context['ctrs2'] = ctrs2
        context['ctrs3'] = ctrs3
        context['date1'] = date1
        context['date2'] = date2
        context['date3'] = date3
        context['total_cost'] = total_cost
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


class UpdateListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Progress
    template_name = 'update_list.html'
    context_object_name = 'update_list'

    # template_name = 'update_list.html'

    # def get(self, request, *args, **kwargs):
    #     print(request.GET)
    #     queryset = Progress.objects.all()
    #     ctx = {
    #         'update_list': queryset
    #     }
    #     return self.render_to_response(ctx)


class UpdateView(LoginRequiredMixin, TemplateView):
    # login_url = settings.LOGIN_URL
    template_name = 'progress_update.html'
    queryset = Progress.objects.all()
    pk_url_kwargs = 'pk'

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


class ProgressUpdate(FormMixin, DetailView,TemplateView):

    template_name = 'progress_update.html'
    model = Progress
    form_class = UpdateForm

    queryset = Progress.objects.all()
    pk_url_kwargs = 'pk'

    # context_object_name = 'user'
    # queryset = Intake.objects.all()

    # DetailView와 FormView를 동시에 사용하기 위한 코드 추가
    def get_success_url(self):
        return reverse('update', kwargs={'pk': self.object.id})

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

        # self.object = self.get_object()
        # form = self.get_form()
        # if form.is_valid():
        #     return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)

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
                messages.success(self.request, '입력 내용이 변경되었습니다.')
            else:
                messages.error(self.request, '알 수 없는 요청입니다.', extra_tags='danger')

            return HttpResponseRedirect('/update/')

        ctx = {
            'prog': self.get_object() if action == 'update' else None
        }
        return self.render_to_response(ctx)


    def form_valid(self, form):
        form.save()
        return super(ProgressUpdate, self).form_valid(form)


# class UpdateDetailView(TemplateView):
#     template_name = 'update_detail.html'
#     queryset = Progress.objects.all()
#     pk_url_kwargs = 'progress_id'

#     def get_object(self, queryset=None):
#         queryset = queryset or self.queryset
#         pk = self.kwargs.get(self.pk_url_kwargs)
#         article = queryset.filter(pk=pk).first()

#         if not article:
#             raise Http404('invalid pk')
#         return article

#     def get(self, request, *args, **kwargs):
#         prog = self.get_object()

#         ctx = {
#             'getplan': prog
#         }
#         return self.render_to_response(ctx)


class ProgressUpdateView(UpdateView):
    model = Progress
    fields = '__all__'
    form_class = ProgressForm
    template_name = 'progress_update.html'
    # template_name_suffix = '_update_form'



class PivotByMonth(DetailView):
    template_name = 'pivot.html'
    model = Progress

    def get_context_data(self, **kwargs):
        test = Progress.objects.filter(getplan_date__month='08').aggregate(med_A=Sum('inmedical_A_sum'))
        context = super().get_context_data(**kwargs)
        # self.kwargs['pk']를 통해서 url에서 pk값을 받을 수 있습니다.
        # url은 `path('<pk>/', PhotoView.as_view())으로 구현되어있어서 해당 pk 부분을 받아옵니다.`
        # context['photo_list'] = Photo.objects.filter(album_id=self.kwargs['pk'])
        return context


def statistics(request):
    January = Progress.objects.filter(getplan_date__month='01') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    February = Progress.objects.filter(getplan_date__month='02') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    March = Progress.objects.filter(getplan_date__month='03') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    April = Progress.objects.filter(getplan_date__month='04') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    May = Progress.objects.filter(getplan_date__month='05') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    June = Progress.objects.filter(getplan_date__month='06') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    July = Progress.objects.filter(getplan_date__month='07') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    August = Progress.objects.filter(getplan_date__month='08') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    September = Progress.objects.filter(getplan_date__month='09') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    October = Progress.objects.filter(getplan_date__month='10') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    November = Progress.objects.filter(getplan_date__month='11') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    December = Progress.objects.filter(getplan_date__month='12') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    
    Total = Progress.objects \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    
    context = {
        'mon_1':January, 'mon_2':February, 'mon_3':March, 'mon_4':April, 'mon_5':May, 'mon_6':June, 'mon_7':July,
        'mon_8': August,'mon_9':September, 'mon_10':October, 'mon_11':November, 'mon_12':December, 'total':Total}
    return render(request, 'pivot.html', context)


def statistics_2019(request):
    January = Progress.objects.filter(getplan_date__month='01').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    February = Progress.objects.filter(getplan_date__month='02').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    March = Progress.objects.filter(getplan_date__month='03').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    April = Progress.objects.filter(getplan_date__month='04').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    May = Progress.objects.filter(getplan_date__month='05').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    June = Progress.objects.filter(getplan_date__month='06').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    July = Progress.objects.filter(getplan_date__month='07').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    August = Progress.objects.filter(getplan_date__month='08').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    September = Progress.objects.filter(getplan_date__month='09').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    October = Progress.objects.filter(getplan_date__month='10').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    November = Progress.objects.filter(getplan_date__month='11').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    December = Progress.objects.filter(getplan_date__month='12').filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    
    Total = Progress.objects.filter(getplan_date__year='2019') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    
    context = {
        'mon_1':January, 'mon_2':February, 'mon_3':March, 'mon_4':April, 'mon_5':May, 'mon_6':June, 'mon_7':July,
        'mon_8': August,'mon_9':September, 'mon_10':October, 'mon_11':November, 'mon_12':December, 'total':Total}
    return render(request, 'pivot_2019.html', context)


def statistics_2020(request):
    January = Progress.objects.filter(getplan_date__month='01').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    February = Progress.objects.filter(getplan_date__month='02').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    March = Progress.objects.filter(getplan_date__month='03').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    April = Progress.objects.filter(getplan_date__month='04').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    May = Progress.objects.filter(getplan_date__month='05').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    June = Progress.objects.filter(getplan_date__month='06').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    July = Progress.objects.filter(getplan_date__month='07').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    August = Progress.objects.filter(getplan_date__month='08').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))

    September = Progress.objects.filter(getplan_date__month='09').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    October = Progress.objects.filter(getplan_date__month='10').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    November = Progress.objects.filter(getplan_date__month='11').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    December = Progress.objects.filter(getplan_date__month='12').filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    
    Total = Progress.objects.filter(getplan_date__year='2020') \
        .aggregate(A1 = Sum('inmedical_A_sum'), A2 = Sum('inmedical_B_sum'), A3 = Sum('inmedical_C_sum'),A4 = Sum('inmedical_D_sum'), A5 = Sum('inmedical_E_sum'), A6 = Sum('inmedical_F_sum'),
        B1 = Sum('inmental_A_sum'), B2 = Sum('inmental_B_sum'), B3 = Sum('inmental_C_sum'),
        C1 = Sum('incase_A_sum'), C2 = Sum('incase_B_sum'), C3 = Sum('incase_C_sum'),
        total_A = Sum('inmedical_A_sum')+Sum('inmedical_B_sum')+Sum('inmedical_C_sum')+Sum('inmedical_D_sum')+Sum('inmedical_E_sum')+Sum('inmedical_F_sum'),
        total_B = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum'),
        total_C = Sum('incase_A_sum') + Sum('incase_B_sum') + Sum('incase_C_sum'))
    
    context = {
        'mon_1':January, 'mon_2':February, 'mon_3':March, 'mon_4':April, 'mon_5':May, 'mon_6':June, 'mon_7':July,
        'mon_8': August,'mon_9':September, 'mon_10':October, 'mon_11':November, 'mon_12':December, 'total':Total}
    return render(request, 'pivot_2020.html', context)



def report(request):

    to_date = request.GET.get('to_date')
    from_date = request.GET.get('from_date')
    
   
    A = Progress.objects.filter(getplan_date__range=[from_date, to_date]).aggregate(A1_1 = Sum('inmedical_A1_YN_1'), A1_2 = Sum('inmedical_A2_YN_1'), A1_3 = Sum('inmedical_A3_YN_1'), A2 = Sum('inmedical_A1_YN_2'),
        A3 = Sum('inmedical_E_sum'), A4_1 = Sum('inmedical_D_sum'), A4_2 = Sum('inmedical_C_sum'), A4_3 = Sum('inmedical_B_sum'),
        A4_4 = Sum('inmedical_F2_YN'), A4_5 = Sum('inmedical_F3_YN'), A4_6 = Sum('inmedical_F1_YN') + Sum('inmedical_F4_YN'),A5 = Sum('inmedical_G_sum'),
        # total = Sum('inmedical_A1_YN_1') + Sum('inmedical_A2_YN_1') + Sum('inmedical_A3_YN_1') + Sum('inmedical_A1_YN_2') + Sum('inmedical_E_sum') + Sum('inmedical_D_sum') + Sum('inmedical_C_sum') + Sum('inmedical_B_sum') + Sum('inmedical_F2_YN') + Sum('inmedical_F3_YN') + Sum('inmedical_F1_YN') + Sum('inmedical_F4_YN') + Sum('inmedical_G_sum')
        )
    if A['A1_1'] is None:A['A1_1'] = 0
    if A['A1_2'] is None:A['A1_2'] = 0
    if A['A1_3'] is None:A['A1_3'] = 0
    if A['A2'] is None:A['A2'] = 0

    if A['A3'] is None:A['A3'] = 0
    if A['A4_1'] is None:A['A4_1'] = 0
    if A['A4_2'] is None:A['A4_2'] = 0
    if A['A4_3'] is None:A['A4_3'] = 0
    if A['A5'] is None:A['A5'] = 0

    if A['A4_4'] is None:A['A4_4'] = 0
    if A['A4_5'] is None:A['A4_5'] = 0
    if A['A4_6'] is None:A['A4_6'] = 0
    A_count = A['A1_1'] + A['A1_2'] + A['A1_3'] + A['A2'] + A['A3'] + A['A4_1'] + A['A4_2'] + A['A4_3'] + A['A4_4'] + A['A4_5'] + A['A4_6'] + A['A5']
    A_people = A['A1_1'] + A['A1_2'] + A['A1_3'] + A['A2'] + A['A3'] + A['A4_1'] + A['A4_2'] + A['A4_3'] + A['A4_4'] + A['A4_5'] + A['A4_6'] + A['A5']
    
    B = Progress.objects.filter(getplan_date__range=[from_date, to_date]).aggregate(B_1 = Sum('inmental_A_sum') + Sum('inmental_B_sum'), B_2 = Sum('incase_A_sum'), B_3 = Sum('inmental_C_sum'),
        total = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum') + Sum('incase_A_sum') )

    D = Progress.objects.filter(getplan_date__range=[from_date, to_date]).aggregate(D_1 = Sum('incase_C2_YN'), D_2 = Sum('incase_C1_YN') + Sum('incase_C3_YN') + Sum('incase_C4_YN'), total = Sum('incase_C1_YN') + Sum('incase_C1_YN') + Sum('incase_C3_YN') + Sum('incase_C4_YN') )

    # C
    Q1 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='성매매예방교육연극(중학교)').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    Q2 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='기관 실무자교육').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    Q3 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='성교육장이용').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    if Q1['count'] is None:Q1['count'] = 0
    if Q2['count'] is None:Q2['count'] = 0
    if Q3['count'] is None:Q3['count'] = 0
    if Q1['people'] is None:Q1['people'] = 0
    if Q2['people'] is None:Q2['people'] = 0
    if Q3['people'] is None:Q3['people'] = 0
    C_count = Q1['count'] + Q2['count'] + Q3['count']
    C_people = Q1['people'] + Q2['people'] + Q3['people']
    # E
    Q4 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='사람유두종바이러스 예방접종 특화').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    Q5 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='찾아가는 성건강교육').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    Q6 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='성건강교육(1:1 / 소그룹)').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    Q7 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='생리대/기타여성용품/성건강수첩 배분').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    if Q4['count'] is None:Q4['count'] = 0
    if Q5['count'] is None:Q5['count'] = 0
    if Q6['count'] is None:Q6['count'] = 0
    if Q7['count'] is None:Q7['count'] = 0
    if Q4['people'] is None:Q4['people'] = 0
    if Q5['people'] is None:Q5['people'] = 0
    if Q6['people'] is None:Q6['people'] = 0
    if Q7['people'] is None:Q7['people'] = 0
    E_count = Q4['count'] + Q5['count'] + Q6['count'] + Q7['count']
    E_people = Q4['people'] + Q5['people'] + Q6['people'] + Q7['people']
    # F
    Q8 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='홍보(전화/문자/홈피/SNS 등)').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    Q9 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='네트워크 및 사업협력/후원발굴.관리').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    Q10 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='직원교육/만족도조사/자원봉사 등').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    if Q8['count'] is None:Q8['count'] = 0
    if Q9['count'] is None:Q9['count'] = 0
    if Q10['count'] is None:Q10['count'] = 0
    if Q8['people'] is None:Q8['people'] = 0
    if Q9['people'] is None:Q9['people'] = 0
    if Q10['people'] is None:Q10['people'] = 0
    F_count = Q8['count'] + Q9['count'] + Q10['count']
    F_people = Q8['people'] + Q9['people'] + Q10['people']

    # G
    Q11 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='임신').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    Q12= Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='성건강').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    Q13 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='기타').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
    if Q11['count'] is None:Q11['count'] = 0
    if Q12['count'] is None:Q12['count'] = 0
    if Q13['count'] is None:Q13['count'] = 0
    if Q11['people'] is None:Q11['people'] = 0
    if Q12['people'] is None:Q12['people'] = 0
    if Q13['people'] is None:Q13['people'] = 0
    G_count = Q11['count'] + Q12['count'] + Q13['count']
    G_people = Q11['people'] + Q12['people'] + Q13['people']


    if B['total'] is None:B['total']=0
    if D['total'] is None:D['total']=0

    Total_count = A_count + B['total'] + C_count + D['total'] + E_count + F_count + G_count
    Total_people = A_people + B['total'] + C_people + D['total'] + E_people + F_people + G_people

    context = {'A': A, 'A_count':A_count, 'A_people':A_people, 'B':B, 'D':D, 'C_count':C_count, 'C_people':C_people,'E_count':E_count, 
    'E_people':E_people,'F_count':F_count, 'F_people':F_people,'G_count':G_count, 'G_people':G_people, 'Count':Total_count, 'People':Total_people,
    'Q1':Q1, 'Q2':Q2, 'Q3':Q3, 'Q4':Q4,'Q5':Q5,'Q6':Q6,'Q7':Q7,'Q8':Q8,'Q9':Q9,'Q10':Q10, 'Q11':Q11, 'Q12':Q12, 'Q13':Q13}
    return render(request, 'report.html', context)


# class Pdf(View):
    
#     def get(self, request):
#         to_date = request.GET.get('to_date')
#         from_date = request.GET.get('from_date')
        
    
#         A = Progress.objects.filter(getplan_date__range=[from_date, to_date]).aggregate(A1_1 = Sum('inmedical_A1_YN_1'), A1_2 = Sum('inmedical_A2_YN_1'), A1_3 = Sum('inmedical_A3_YN_1'), A2 = Sum('inmedical_A1_YN_2'),
#             A3 = Sum('inmedical_E_sum'), A4_1 = Sum('inmedical_D_sum'), A4_2 = Sum('inmedical_C_sum'), A4_3 = Sum('inmedical_B_sum'),
#             A4_4 = Sum('inmedical_F2_YN'), A4_5 = Sum('inmedical_F3_YN'), A4_6 = Sum('inmedical_F1_YN') + Sum('inmedical_F4_YN'),A5 = Sum('inmedical_G_sum'),
#             # total = Sum('inmedical_A1_YN_1') + Sum('inmedical_A2_YN_1') + Sum('inmedical_A3_YN_1') + Sum('inmedical_A1_YN_2') + Sum('inmedical_E_sum') + Sum('inmedical_D_sum') + Sum('inmedical_C_sum') + Sum('inmedical_B_sum') + Sum('inmedical_F2_YN') + Sum('inmedical_F3_YN') + Sum('inmedical_F1_YN') + Sum('inmedical_F4_YN') + Sum('inmedical_G_sum')
#             )
#         if A['A1_1'] is None:A['A1_1'] = 0
#         if A['A1_2'] is None:A['A1_2'] = 0
#         if A['A1_3'] is None:A['A1_3'] = 0
#         if A['A2'] is None:A['A2'] = 0

#         if A['A3'] is None:A['A3'] = 0
#         if A['A4_1'] is None:A['A4_1'] = 0
#         if A['A4_2'] is None:A['A4_2'] = 0
#         if A['A4_3'] is None:A['A4_3'] = 0
#         if A['A5'] is None:A['A5'] = 0

#         if A['A4_4'] is None:A['A4_4'] = 0
#         if A['A4_5'] is None:A['A4_5'] = 0
#         if A['A4_6'] is None:A['A4_6'] = 0
#         A_count = A['A1_1'] + A['A1_2'] + A['A1_3'] + A['A2'] + A['A3'] + A['A4_1'] + A['A4_2'] + A['A4_3'] + A['A4_4'] + A['A4_5'] + A['A4_6'] + A['A5']
#         A_people = A['A1_1'] + A['A1_2'] + A['A1_3'] + A['A2'] + A['A3'] + A['A4_1'] + A['A4_2'] + A['A4_3'] + A['A4_4'] + A['A4_5'] + A['A4_6'] + A['A5']
        
#         B = Progress.objects.filter(getplan_date__range=[from_date, to_date]).aggregate(B_1 = Sum('inmental_A_sum') + Sum('inmental_B_sum'), B_2 = Sum('incase_A_sum'), B_3 = Sum('inmental_C_sum'),
#             total = Sum('inmental_A_sum') + Sum('inmental_B_sum') + Sum('inmental_C_sum') + Sum('incase_A_sum') )

#         D = Progress.objects.filter(getplan_date__range=[from_date, to_date]).aggregate(D_1 = Sum('incase_C2_YN'), D_2 = Sum('incase_C1_YN') + Sum('incase_C3_YN') + Sum('incase_C4_YN'), total = Sum('incase_C1_YN') + Sum('incase_C1_YN') + Sum('incase_C3_YN') + Sum('incase_C4_YN') )

#         # C
#         Q1 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='성매매예방교육연극(중학교)').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         Q2 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='기관 실무자교육').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         Q3 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='성교육장이용').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         if Q1['count'] is None:Q1['count'] = 0
#         if Q2['count'] is None:Q2['count'] = 0
#         if Q3['count'] is None:Q3['count'] = 0
#         if Q1['people'] is None:Q1['people'] = 0
#         if Q2['people'] is None:Q2['people'] = 0
#         if Q3['people'] is None:Q3['people'] = 0
#         C_count = Q1['count'] + Q2['count'] + Q3['count']
#         C_people = Q1['people'] + Q2['people'] + Q3['people']
#         # E
#         Q4 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='사람유두종바이러스 예방접종 특화').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         Q5 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='찾아가는 성건강교육').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         Q6 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='성건강교육(1:1 / 소그룹)').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         Q7 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='생리대/기타여성용품/성건강수첩 배분').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         if Q4['count'] is None:Q4['count'] = 0
#         if Q5['count'] is None:Q5['count'] = 0
#         if Q6['count'] is None:Q6['count'] = 0
#         if Q7['count'] is None:Q7['count'] = 0
#         if Q4['people'] is None:Q4['people'] = 0
#         if Q5['people'] is None:Q5['people'] = 0
#         if Q6['people'] is None:Q6['people'] = 0
#         if Q7['people'] is None:Q7['people'] = 0
#         E_count = Q4['count'] + Q5['count'] + Q6['count'] + Q7['count']
#         E_people = Q4['people'] + Q5['people'] + Q6['people'] + Q7['people']
#         # F
#         Q8 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='홍보(전화/문자/홈피/SNS 등)').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         Q9 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='네트워크 및 사업협력/후원발굴.관리').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         Q10 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='직원교육/만족도조사/자원봉사 등').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         if Q8['count'] is None:Q8['count'] = 0
#         if Q9['count'] is None:Q9['count'] = 0
#         if Q10['count'] is None:Q10['count'] = 0
#         if Q8['people'] is None:Q8['people'] = 0
#         if Q9['people'] is None:Q9['people'] = 0
#         if Q10['people'] is None:Q10['people'] = 0
#         F_count = Q8['count'] + Q9['count'] + Q10['count']
#         F_people = Q8['people'] + Q9['people'] + Q10['people']

#         # G
#         Q11 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='임신').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         Q12= Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='성건강').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         Q13 = Program.objects.filter(perfor_date__range=[from_date, to_date]).filter(perfor_program='기타').aggregate(count = Sum('perfor_count'), people = Sum('perfor_people'))
#         if Q11['count'] is None:Q11['count'] = 0
#         if Q12['count'] is None:Q12['count'] = 0
#         if Q13['count'] is None:Q13['count'] = 0
#         if Q11['people'] is None:Q11['people'] = 0
#         if Q12['people'] is None:Q12['people'] = 0
#         if Q13['people'] is None:Q13['people'] = 0
#         G_count = Q11['count'] + Q12['count'] + Q13['count']
#         G_people = Q11['people'] + Q12['people'] + Q13['people']


#         if B['total'] is None:B['total']=0
#         if D['total'] is None:D['total']=0

#         Total_count = A_count + B['total'] + C_count + D['total'] + E_count + F_count + G_count
#         Total_people = A_people + B['total'] + C_people + D['total'] + E_people + F_people + G_people

#         context = {'A': A, 'A_count':A_count, 'A_people':A_people, 'B':B, 'D':D, 'C_count':C_count, 'C_people':C_people,'E_count':E_count, 
#         'E_people':E_people,'F_count':F_count, 'F_people':F_people,'G_count':G_count, 'G_people':G_people, 'Count':Total_count, 'People':Total_people,
#         'Q1':Q1, 'Q2':Q2, 'Q3':Q3, 'Q4':Q4,'Q5':Q5,'Q6':Q6,'Q7':Q7,'Q8':Q8,'Q9':Q9,'Q10':Q10, 'Q11':Q11, 'Q12':Q12, 'Q13':Q13}
#         return Render.render('report.html', context)