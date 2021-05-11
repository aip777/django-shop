from django import forms
from .models import Order
# external admin form start

class AddOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddOrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

            self.fields['products'].widget.attrs.update({
                'style': 'height:calc(11.5em + 0.75rem + 2px)',
                 
            })

    class Meta:
        model = Order
        fields = ('products',)


class EditOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditOrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' 

            self.fields['products'].widget.attrs.update({
                'style': 'height:calc(11.5em + 0.75rem + 2px)',
                 
            })
    
    class Meta:
        model = Order
        fields = ('customer', 'products',)