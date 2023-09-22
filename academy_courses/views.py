from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Course, Slider, Video, Comment
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .forms import CourseForm, VideoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    slider = Slider.objects.all()


    return render(
        request,
        'index.html',
        {
            'slider': slider,
        }
    )


def about(request):
    aboutus_image = Slider.objects.first()

    return render(request, 'about.html', {'image': aboutus_image,})


def course(request):

    query = request.GET.get('query')

    where = {}
    if query:
        where['name__icontains'] = query

    course = Course.objects.filter(**where)

    return render(
        request,
        'course.html',
        {
            'courses': course
        }
    )


@login_required
def course_list(request, pk):

    query = request.GET.get('query')

    where = {}
    if query:
        where['name__icontains'] =  query

    video = Video.objects.filter(course=pk, **where).select_related('course')
    course = Course.objects.filter(pk=pk)

    return render(
        request,
        'course_list.html',
        {
            'videos': video,
            'cou': course,
        }
    )


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Video
    template_name = 'course_page.html'
    context_object_name = 'video'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/create.html'
    success_url = reverse_lazy('course')


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/update.html'
    success_url = reverse_lazy('course')


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'course/delete.html'
    success_url = reverse_lazy('course')


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'video/create.html'
    

    def get_success_url(self):
        return reverse('course_list', args=[self.object.course_id])


class VideoUpdateView(LoginRequiredMixin, UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'video/update.html'

    def get_success_url(self):
        return reverse('course_list', args=[self.object.course_id])


class VideoDeleteView(LoginRequiredMixin, DeleteView):
    model = Video
    template_name = 'video/delete.html'
    
    def get_success_url(self):
        return reverse('course_list', args=[self.object.course_id])
    

class CommentCreateView(CreateView):
    model = Comment
    fields = ['video', 'user', 'message']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('course_page', args=[self.object.video.id]) 
    
    # def test_func(self):
    #     project_id = self.request.POST.get('project', '')
    #     return models.Project.objects.get(pk=project_id).user_id == self.request.user.id

    

class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse('course_page', args=[self.object.video.id]) 
    