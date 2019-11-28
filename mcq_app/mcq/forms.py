from django.forms import ModelForm

from .models import Category, Question, User, Attempt

class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ("Category",)

class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ('Category', 'Question', 'Answer', 'Options', 'Weight')

class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ('FirstName', 'LastName', 'Email')

class UserAttemptForm(ModelForm):

    class Meta:
        model = Attempt
        fields = ('User_Email',)
