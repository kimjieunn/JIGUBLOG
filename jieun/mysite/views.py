from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
import requests

class HomeView(TemplateView):
    template_name = 'home.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True #False로 바꾸면 로그인 페이지로 이동
    permission_denied_message = "해당 내용을 작성한 사용자만이 수정 및 삭제가 가능합니다."

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class CumtomAPI_TV(TemplateView):
    template_name = 'custom_page.html'

    def get_context_data(delf, **kwargs):
        context = super().get_context_data(**kwargs)
        key = 'a782a0f5f79c237d86971498f3ad725c'
        date = '20220901'
        url='http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}&targetDt={}'.format(key, date)

        response = requests.get(url)
        context['boxOfficeResult'] = response.json()['boxOfficeResult']

        return context
