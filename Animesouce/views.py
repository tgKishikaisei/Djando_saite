from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.views.generic import DeleteView, DetailView, UpdateView

from .forms import NewForm
from .models import Creators, New


# Создавать, редактировать и удалять статьи могут только сотрудники (is_staff),
# вход через /admin/login/.
def is_staff(user):
    return user.is_active and user.is_staff


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return is_staff(self.request.user)


def creators(request):
    creat = Creators.objects.order_by('date')
    return render(request, 'souce/souce.html', {'creat': creat})


class NewsDetailView(DetailView):
    model = New
    template_name = 'souce/details_view.html'
    context_object_name = 'article'


class NewsDeleteView(StaffRequiredMixin, DeleteView):
    model = New
    success_url = '/creators/new/'
    template_name = 'souce/news-delete.html'


class NewsUpdatelView(StaffRequiredMixin, UpdateView):
    model = New
    template_name = 'souce/create.html'
    form_class = NewForm


def new(request):
    news = New.objects.order_by('-date')
    return render(request, 'souce/new.html', {'new': news})


@login_required
@user_passes_test(is_staff)
def create(request):
    error = ''
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('news-detail', pk=article.pk)
        # Форма с ошибками возвращается пользователю, чтобы он видел, что исправить
        error = 'Статья не добавлена: исправьте ошибки в форме'
    else:
        form = NewForm()
    return render(request, 'souce/create.html', {'form': form, 'error': error})
