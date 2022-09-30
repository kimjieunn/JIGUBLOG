from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse
from .models import Video
from mysite.views import OwnerOnlyMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def video(request):
	Tut = Video.objects.all()
	context = {
	'Tut': Tut,
	}
	return  render(request, 'video/video_list.html', context)


#LoginRequiredMixin -> 로그인한 사용자가 아니면 로그인 페이지로 이동
class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    template_name ='video/video_form.html'
    fields = ['title', 'text', 'video']
    success_url = reverse_lazy('video:video')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


#object_list -> 현재 로그인한 사용자가 작성한 Site
class VideoChangeLV(LoginRequiredMixin, ListView):
    template_name = 'video/video_change_list.html'
    fields = ['title', 'text', 'video']

    def get_queryset(self):
        return Video.objects.filter(owner = self.request.user)

#OwnerOnlyMixin -> 작성자만이 수정할 수 있도록
class VideoUpdateView(OwnerOnlyMixin, UpdateView):
    model = Video
    fields = ['title', 'text', 'video']
    success_url = reverse_lazy('video:video')
    template_name = 'video/video_form.html'

#OwnerOnlyMixin -> 작성자만이 삭제할 수 있도록
class VideoDeleteView(OwnerOnlyMixin, DeleteView):
    model = Video
    success_url = reverse_lazy('video:video')
    template_name = 'video/video_confirm_delete.html'