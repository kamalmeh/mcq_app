from django.http import HttpRequest
from django.shortcuts import render

from .models import Test, TestQuestion, Question, Category

def create_test_view(request):
    category = Category()
    categories = category.get_all_categories()

    test = Test()
    tests = test.get_all_tests()

    questionsObject = Question()
    questions = questionsObject.get_test_questions_as_list()

    q_list = get_context_questions(questions)

    context = {'categories': categories, 'tests' : tests, 'questions': q_list}

    if request.method=='GET':
        return render(request, 'create_test.html',context)
    elif request.method=='POST':
        q_list_checked = ""
        for question in questions:
            if str(question['id']) in request.POST:
                if q_list_checked == "":
                    q_list_checked = str(question['id'])
                else :
                    q_list_checked = q_list_checked + "," + str(question['id'])
        category_name = Category(request.POST['category'])
        test_name = request.POST['test_name']
        test_description = request.POST['test_description']
        new_record = Test(Category_Id=category_name, Test_Name=test_name, Test_Description=test_description)
        new_record.save()
        test_questions = TestQuestion(test_Id=new_record, test_Question=q_list_checked)
        test_questions.save()
        return render(request, 'redirect.html', context={'url':'admin_view.html'})

def edit_test_view(request):
    tests = Test.objects.values()
    context = {'tests':tests}
    if request.method=='GET':
        return render(request, 'edit_test.html', context)
    elif request.method=='POST':
        test_id = int(request.POST['test_name'])
        test_questions = TestQuestion.objects.filter(test_Id_id=test_id).values()
        all_questions = Question.objects.values()
        context = {'test_id': test_id, 'tests': tests, 'test_questions': test_questions, 'questions': all_questions}
        if "retrieve" in request.POST:
            return render(request, 'edit_test.html', context={'url':'admin_view.html'})
        else :
            return render(request, 'redirect.html', context={'url':'admin_view.html'})
    # return render(request, 'redirect.html', context={'url':'admin_view.html'})

def admin_view(request):
    return render(request, 'admin.html', {})

def home_view(request):
    return render(request, 'index.html', {'test':'test_user'})

def test_view(request):
    testQ = TestQuestion()

    if request.method=='GET':
#Get the all questions to display
        questions = []
        if 'id' in request.GET:
            test_id=int(request.GET['id'])
            q_ids = testQ.get_test_questions_as_list(test_id)            
#Create context data for the template to render
            questions = get_context_questions_from_ids(q_ids)
        context_questions = get_context_questions(questions)
        context = {'questions' : context_questions }
    elif request.method=='POST':
        if request.GET.get('id') != None:
            test_id=int(request.GET['id'])
            q_ids = testQ.get_test_questions_as_list(test_id)
#Create context data for the template to render
            questions = get_context_questions_from_ids(q_ids)
        context_questions = get_context_questions(questions)
        context = {'questions' : context_questions }
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

def get_context_questions(questions):
#I had to do below because the original QuerySet is immutable, hence create new list and passed to template
    context_questions = []
    for question in questions:
#Options are the main reason to do this logic, this list will be used to rendomize the options on every load.
        temp_str = question['Options'].replace("\r\n", "\n")           #This is due to windows carriage written character
        question['Options'] = temp_str.split("\n")
        context_questions.append(question)
    return context_questions

def get_context_questions_from_ids(Q_ids):
    context_questions = []
    for q_id in Q_ids:
        context_questions.append(Question.objects.values().filter(id=int(q_id))[0])
    return context_questions