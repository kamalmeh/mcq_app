from django_tables2 import tables
from .models import Attempt

class AttemptTable(tables.Table):
    User_Email = tables.columns.Column(accessor='User_Email.Email', verbose_name="User Email")
    Test_Id = tables.columns.Column(accessor='Test_Id.Test_Name', verbose_name="Test ID")
    Test_Status = tables.columns.Column(accessor='Test_Status.Status_Name', verbose_name="Test Status")
    class Meta:
        model = Attempt
        template_name = "django_tables2/semantic.html"
        # fields = ('id', 'Email', 'Test_Id', 'Test_Status', 'Score', 'Timestamp')
        # sequence = ('id', 'Email', 'Test_Id', 'Test_Status', 'Score', 'Timestamp')