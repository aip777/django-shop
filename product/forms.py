from django import forms
from .models import Category, Products
# external admin form start

class AddCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = ('category_name',)

class EditCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditCategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
 
    class Meta:
        model = Category
        fields = ('category_name',)


class AddProductsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddProductsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Products
        fields = ('name','code','category','price','current_stock')

class EditProductsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProductsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
 
    class Meta:
        model = Products
        fields = ('name','code','category','price','current_stock')


  