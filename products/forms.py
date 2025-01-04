from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from django import forms

from .models import Product, Category, Image, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = [
            'primary_img',
            'secondary_img',
            'tertiary_img',
        ]
        help_texts = {
            'primary_img': mark_safe(_(
                '<small style="color:red">Please be advised that if you \
                delete (clear) your custom primary image and do not provide \
                a replacement, all images for this product will be \
                permanently deleted.</small>')),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
