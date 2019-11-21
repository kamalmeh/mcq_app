from django.http import HttpRequest
from django.shortcuts import render

from .models import Question

def home_view(request):
    return render(request, 'index.html', {'test':'test_user'})

def test_view(request):
    tests = Question()
    questions = tests.get_test_questions_as_list()

#I had to do below because the original QuerySet is immutable, hence create new list and passed to template
    context_questions = []
    for question in questions:
        print(question)
#Options are the main reason to do this logic, this list will be used to rendomize the options on every load.
        temp_str = question['Options'].replace("\r\n", "\n")           #This is due to windows carriage written character
        question['Options'] = temp_str.split("\n")
        context_questions.append(question)
        
#Create context data for the template to render
    context = {'questions' : context_questions }

    if request.method=='GET':
#Get the all questions to display
        return  render(request, 'test.html', context)
    elif request.method=='POST':
        score = 0
        for question in questions:
            formQuestion = request.POST["Question_" + str(question['id'])]
            if question['Question']==formQuestion:
                question['UserAnswered'] = request.POST["Answer_" + str(question['id'])]
                question['CorectAnswer'] = question['Answer']
                if question['Answer']==question['UserAnswered']:
                    score = score + question['Weight']
                # context_questions.append(question)
        
        context = { 'questions' : context_questions, 'score' : score }
        return render(request, 'test.html', context)