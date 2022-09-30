from django.shortcuts import render
from django.views.generic import *
from django.views.generic.dates import *
from blog.models import Post, Category, Site
from django.conf import settings
from django.db.models import Q
from blog.forms import PostSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin


# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 3

class PostDV(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f'{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}'
        context['disqus_title'] = f"{self.object.slug}"
        return context


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    #month_format = '%d' #디폴트 값

class PostMAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'

class PostDAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'

class PostTAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    model = Post
    template_name = 'taggit/taggit_post_list.html'

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

class SearchFV(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains = searchWord) |
                                        Q(description__icontains = searchWord) |
                                        Q(content__icontains = searchWord)).distinct()
        context = {'form': form,
                    'search_term': searchWord,
                    'object_list': post_list
                    }
        return render(self.request, self.template_name, context)

#LoginRequiredMixin -> 로그인한 사용자가 아니면 로그인 페이지로 이동
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'slug', 'description', 'content', 'tags']
    # initial = {'slug': '자동으로-완성되니-적지마세요.'}
    fields = ['title', 'category','image', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

 #object_list -> 현재 로그인한 사용자가 작성한 Post
class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner = self.request.user)
         
#OwnerOnlyMixin -> 작성자만이 수정할 수 있도록
class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    # fields = ['title', 'slug', 'description', 'content', 'tags']
    fields = ['title', 'category', 'image', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:index')

#OwnerOnlyMixin -> 작성자만이 삭제할 수 있도록
class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

class CategoryView(ListView):
    model = Category
    template_name = 'blog/post_category.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name ='blog/post_category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(category = self.kwargs['pk'])
        return context


#LoginRequiredMixin -> 로그인한 사용자가 아니면 로그인 페이지로 이동
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name ='blog/post_category_form.html'
    fields = ['name',]
    success_url = reverse_lazy('blog:category')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


#object_list -> 현재 로그인한 사용자가 작성한 Category
class CategoryChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_category_change_list.html'
    fields = ['name',]

    def get_queryset(self):
        return Category.objects.filter(owner = self.request.user)

#OwnerOnlyMixin -> 작성자만이 수정할 수 있도록
class CategoryUpdateView(OwnerOnlyMixin, UpdateView):
    model = Category
    fields = ['name',]
    success_url = reverse_lazy('blog:category')
    template_name = 'blog/post_category_form.html'

#OwnerOnlyMixin -> 작성자만이 삭제할 수 있도록
class CategoryDeleteView(OwnerOnlyMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('blog:category')
    template_name = 'blog/post_categoey_confirm_delete.html'


class SiteView(ListView):
    model = Site
    template_name = 'blog/post_site.html'

#LoginRequiredMixin -> 로그인한 사용자가 아니면 로그인 페이지로 이동
class SiteCreateView(LoginRequiredMixin, CreateView):
    model = Site
    template_name ='blog/post_site_form.html'
    fields = ['title', 'image', 'url']
    success_url = reverse_lazy('blog:site')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


#object_list -> 현재 로그인한 사용자가 작성한 Site
class SiteChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_site_change_list.html'
    fields = ['title', 'image', 'url']

    def get_queryset(self):
        return Site.objects.filter(owner = self.request.user)

#OwnerOnlyMixin -> 작성자만이 수정할 수 있도록
class SiteUpdateView(OwnerOnlyMixin, UpdateView):
    model = Site
    fields = ['title', 'image', 'url']
    success_url = reverse_lazy('blog:site')
    template_name = 'blog/post_site_form.html'

#OwnerOnlyMixin -> 작성자만이 삭제할 수 있도록
class SiteDeleteView(OwnerOnlyMixin, DeleteView):
    model = Site
    success_url = reverse_lazy('blog:site')
    template_name = 'blog/post_site_confirm_delete.html'