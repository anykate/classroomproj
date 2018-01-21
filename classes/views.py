from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Student, Subject


# Create your views here.
class IndexPageView(ListView):
    model = Student
    template_name = 'classes/index.html'

    try:
        students = Student.objects.all()
        extra_context = {'students': students}

    except Student.DoesNotExist:
        print('First you need to create the records in the database.')
        print('Hence, comment this \'try..except\' block & makemigrations & migrate')


class DetailPageView(ListView):
    model = Subject
    template_name = 'classes/subjects.html'

    def get_context_data(self, **kwargs):
        context = super(DetailPageView, self).get_context_data(**kwargs)
        context['subjects'] = Subject.objects.filter(student_id=self.kwargs.get('student_id'))

        if (context['subjects']):
            return context

        else:
            print('error')
            redirect('/')   # I want to redirect to root url(index) in this condition,
                            # however, this is not working ~Aniket Aryamane
