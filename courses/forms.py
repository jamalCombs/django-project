from django import forms
from .models import Course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'summary'
        ]

    def save(self):
        new_course = Course.objects.create(
            title = self.cleaned_data['title'],
            summary = self.cleaned_data['summary']
        )

        return new_course 