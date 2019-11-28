from django.db import models

# models are basically database in SQLite. We can change it to any other database we like by changing the settings.py

class Category(models.Model):
#Category Id is inbuilt
    Category    = models.CharField(max_length=250, blank=True, unique=True, null=True, verbose_name="Category")
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.Category
    
    def get_all_categories(self):
        categories = Category.objects.values()
        return categories
    
    def get_name(self, id):
        name = ""
        for category in Category.objects.values():
            if category.id == id:
                name = category.Category
        return name

class Question(models.Model):
#Question Id is inbuilt
    Category    = models.ForeignKey(Category, null=True, blank=True, verbose_name="Category", on_delete=models.CASCADE)
    Question    = models.TextField(blank=False, null=False)
    Answer      = models.CharField(blank=False, null=False, max_length=255, help_text="Answer is matched literally, any single character difference will result in mismatch")
#We can change to models.ListCharField() in django_mysql.models. We can use new line character for separating four options, temporarily in sqlite
    Options     = models.TextField(blank=False, null=False, help_text="Line Feed/New Line separated Options")
    Weight      = models.IntegerField(default=1, null=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
    
    def get_test_questions_as_list(self):
        questions = Question.objects.values()
        return questions

class Test(models.Model):
#Test Id is inbuilt
    Category_Id = models.ForeignKey(Category, on_delete=models.CASCADE)
    Test_Name   = models.CharField(null=False, blank=False, max_length=255, default="Provide Test Name", unique=True)
    Test_Description = models.TextField(default="")

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Tests"

    def edit_test(self):
        pass

    def create_test(self):
        pass

    def get_all_tests(self):
        test_list = []
        tests = Test.objects.values()
        for test in tests:
            test_list.append(test)
        return test_list

    def update_question_set(self, QID_csv_list):
        self(QID_csv_list)

class TestQuestion(models.Model):
#TestQuestions Id is inbuilt
    test_Id         = models.ForeignKey(Test, on_delete=models.CASCADE)
    test_Question   = models.CharField(null=False, blank=False, max_length=255, default="")
    
    class Meta:
        verbose_name = "TestQuestion"
        verbose_name_plural = "TestQuestions"
    
    def get_test_questions_as_list(self, test_id):
        question_list = []
        testQuestions = TestQuestion.objects.values()
        for testQuestion in testQuestions:
            if test_id == testQuestion['test_Id_id']:
                question_list = testQuestion['test_Question'].split(',')
        return question_list

class Status(models.Model):
    Status_Name = models.CharField(null=False, blank=False, unique=True, max_length=255, default="Not Started")

class User(models.Model):
    FirstName = models.CharField(null=False, blank=False, max_length=255, default="First Name")
    LastName = models.CharField(null=False, blank=False, max_length=255, default="Last Name")
    Email = models.EmailField(null=False, blank=False, max_length=255, primary_key=True, default="Email", verbose_name="Email")
    # Test_Id = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Test ID", default=1)

    # class Meta:
    #     unique_together = (('Email','Test_Id'),)

class Attempt(models.Model):
    User_Email = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    Test_Id = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Test ID")
    Total = models.IntegerField(default=0, verbose_name="Total")
    Score   = models.IntegerField(default=0, verbose_name="Score")
    Timestamp = models.DateTimeField(verbose_name="Test Attempt Date & Time", auto_now_add=True)
    Test_Status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, to_field='Status_Name')