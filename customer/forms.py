from django import forms
from .models import Customer
# external admin form start

class AddCustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCustomerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Customer
        fields = ('name','mobile', 'email',)

