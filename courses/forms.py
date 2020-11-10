from django import forms
from .models import Course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'summary'
        ]
        
        labels = {
            "title": '',
            "summary": ''
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder':'Title',
                'class':'form-control'
                }),

            'summary': forms.Textarea(attrs={
                'placeholder':'Description...',
                'class':'form-control',
                'rows':5,
                'cols':1
                })
        }

    def save(self):
        new_course = Course.objects.create(
            title = self.cleaned_data['title'],
            summary = self.cleaned_data['summary']
        )

        return new_course 