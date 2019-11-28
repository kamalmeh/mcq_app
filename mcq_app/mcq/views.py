from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.forms import modelformset_factory
from django.db.models import DateTimeField
from django.utils import timezone

from .models import Test, TestQuestion, Question, Category, User, Attempt, Status
from .forms import CategoryForm, QuestionForm, UserForm, UserAttemptForm
from .tables import AttemptTable

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
        return render(request, 'create_test.html', context)
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
        new_record = None
        try:
            new_record = Test(Category_Id=category_name, Test_Name=test_name, Test_Description=test_description)
            new_record.save()
        except:
            return render(request, 'message.html', {'message': 'Please try with a different test name'})
        test_questions = TestQuestion(test_Id=new_record, test_Question=q_list_checked)
        test_questions.save()
        return render(request, 'redirect.html', context={'url':'admin_view'})

def edit_test_view(request):
    tests = Test.objects.values()
    context = {'tests': tests}
    if request.method=='GET':
        return render(request, 'edit_test.html', context)
    elif request.method=='POST':
        test_id = int(request.POST['test_name'])
        if test_id == 0:
            context['message'] = 'Please select appropriate test to proceed'
        else :
            test_data = Test.objects.filter(id=test_id).values()[0]
            test_name = test_data['Test_Name']
            test_questions_id = TestQuestion.objects.filter(test_Id_id=test_id).values()[0]
            questions = Question.objects.values()
            new_questions = []
            temp_q = {}
            for question in questions:
                temp_q = question.copy()
                for item in test_questions_id['test_Question'].split(','):
                    if question['id'] == int(item):
                        temp_q['checked'] = 'checked'
                        break
                new_questions.append(temp_q)
            context['test_id'] = test_id 
            context['test_name'] = test_name 
            context['questions'] = new_questions

        if "retrieve" in request.POST:
            return render(request, 'edit_test.html', context)
        elif "submit" in request.POST:
            q_list_checked = ""
            for question in questions:
                if str(question['id']) in request.POST:
                    if q_list_checked == "":
                        q_list_checked = str(question['id'])
                    else :
                        q_list_checked = q_list_checked + "," + str(question['id'])
            test_data = TestQuestion.objects.get(test_Id_id=test_id)
            test_data.test_Question=q_list_checked
            test_data.save()
            return render(request, 'redirect.html', context={'url':'admin_view'})

def delete_test_view(request):
    tests = Test.objects.values()
    context = {'tests': tests}
    if request.method=='GET':
        return render(request, 'delete_test.html', context)
    elif request.method=='POST':
        for each_test in tests:
            if str(each_test['id']) in request.POST:
                Test.objects.filter(id=each_test['id']).delete()
        return render(request, 'redirect.html', context={'url':'admin_view'})

def all_test_view(request):
    tests = Test.objects.values()
    context = {'tests': tests}
    return render(request, 'all_tests.html', context)

def add_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return render(request, 'redirect.html', {'url': 'create_test'})
        else:
            return render(request, 'message.html', {'message': 'Please try with difference Category Name'})
    elif request.method == 'GET':
        return render(request, 'add_category.html', {'form': CategoryForm()})

def add_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_form.save()
            return render(request, 'redirect.html', {'url': 'admin_view'})
        else:
            return render(request, 'message.html', {'message': 'Unable to save Question in Question Bank<br>Please try again later'})
    elif request.method == 'GET':
        return render(request, 'add_question.html', {'form': QuestionForm()})

def assign_test_view(request):
    if request.method == 'GET':
        user_selection_form = UserAttemptForm()
        test_list = Test.objects.values()
        return render(request, 'assign_test.html', {'form': user_selection_form, 'tests': test_list})
    elif request.method == 'POST':
        if 'User_Email' in request.POST:
            email = request.POST['User_Email']
            tests = Test.objects.values()
            for test in tests:
                if str(test['id']) in request.POST:
                    single_test = Test.objects.get(id=test['id'])
                    user_info = User.objects.get(Email=email)
                    status = Status.objects.get(Status_Name="Not Started")
                    q_list = TestQuestion.objects.filter(test_Id=single_test).values_list('test_Question', flat=True)
                    total = 0
                    for q in q_list[0].split(','):
                        q_weight = Question.objects.filter(id=q).values('Weight')[0]
                        total = total + int(q_weight['Weight'])
                    attempt_record = Attempt(User_Email=user_info, Test_Id=single_test, Test_Status=status, Total=total, Timestamp=timezone.now())
                    attempt_record.save()
                    return render(request, 'message.html', {'message': 'Test Assigned', 'url': request.scheme + "://" + request.get_host() + "/test?user=" + email + "&id=" + str(test['id'])})
        return render(request, 'redirect.html', {'url': 'admin_view'})

def add_user_view(request):
    userForm = ""
    if request.method == 'GET':
        userForm = UserForm()
    elif request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return render(request, 'redirect.html', {'url': 'admin_view'})
    return render(request, 'add_user.html', {'form': userForm})

def display_error_view(request):
    return render(request, 'message.html', {'message': '404 ERROR - Page Not Found', 'url': request.scheme + "://" + request.get_host()})
    # return redirect(reverse_lazy('error'))

def edit_question_view(request):
    question_form = None
    if request.method == 'GET':
        questions = Question.objects.values()
        context = { 'questions': questions }
        return render(request, 'edit_question.html', context)
    elif request.method == 'POST':
        if 'question' in request.POST:
            question = Question.objects.get(Question=request.POST['question'])
            question_form = QuestionForm(instance=question)
        else :
            question = Question.objects.get(Question=request.POST['Question'])
            question_form = QuestionForm(request.POST, instance=question)
            if question_form.is_valid():
                question_form.save()
                return render(request, 'redirect.html', {'url': 'admin_view'})
    return render(request, 'edit_question.html', {'form': question_form})

def admin_view(request):
    return render(request, 'admin.html', {})

def home_view(request):
    return render(request, 'message.html', {'message': 'Provide user name', 'url': 'For Example: ' + request.scheme + "://" + request.get_host() + '/test?user=<user_name>&id=<test_id>'})

def test_view(request):
    testQ = TestQuestion()
    questions = []
    email = None
    test_id = None
    message = None
    if 'user' in request.GET or 'user' in request.POST:
        email = request.GET['user']
    if 'id' in request.GET or 'id' in request.POST:
        test_id=int(request.GET['id'])

    if request.method=='GET':
        attempt_table = None
#Get the all questions to display
        user_attempt = Attempt.objects.filter(Test_Id_id=test_id, User_Email=email).values()
        if len(user_attempt) > 0 :
            q_ids = testQ.get_test_questions_as_list(test_id)
#Create context data for the template to render
            questions = get_context_questions_from_ids(q_ids)
        else:
            message = "The test is not associated with user"
        attempt_data = Attempt.objects.filter(User_Email_id=email, Test_Id_id=test_id).order_by('User_Email_id')
        attempt_table = AttemptTable(attempt_data)
        context_questions = get_context_questions(questions)
        context = {'questions' : context_questions, 'user': email, 'test_id': test_id, 'attempt_data': attempt_table, 'message': message }
    elif request.method=='POST':
        questions = []
        q_ids = testQ.get_test_questions_as_list(test_id)
#Create context data for the template to render
        questions = get_context_questions_from_ids(q_ids)
        context_questions = get_context_questions(questions)
        context = {'questions' : context_questions }
        score = 0
        total = 0
        for question in questions:
            formQuestion = request.POST["Question_" + str(question['id'])]
            if question['Question']==formQuestion:
                question['UserAnswered'] = request.POST["Answer_" + str(question['id'])]
                question['CorectAnswer'] = question['Answer']
                total = total + question['Weight']
                if question['Answer']==question['UserAnswered']:
                    score = score + question['Weight']
                context_questions.append(question)
        status = Status.objects.get(Status_Name='Not Started')
        try:
            user_attempt = Attempt.objects.get(Test_Id_id=test_id, User_Email_id=email, Test_Status=status)
            if user_attempt.Test_Status == status:
                user_attempt.Test_Status = Status.objects.get(Status_Name='Attempted')
                user_attempt.Timestamp = timezone.now()
                user_attempt.Score = score
                user_attempt.Total = total
                user_attempt.save()
        except:
            user_attempt = Attempt(Test_Id_id=test_id, User_Email_id=email, Test_Status=Status.objects.get(Status_Name='Attempted'), Timestamp=timezone.now(), Total=total, Score=score)
            total = user_attempt.Total
            user_attempt.save()
        
        attempt_data = Attempt.objects.filter(User_Email_id=email, Test_Id_id=test_id).order_by('User_Email_id')
        attempt_table = AttemptTable(attempt_data)

        # context = { 'questions' : context_questions, 'score' : score, 'user': email, 'test_id': test_id, 'attempt_data': attempt_table }
        context = { 'score' : score, 'total': total, 'user': email, 'test_id': test_id, 'attempt_data': attempt_table }
    
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