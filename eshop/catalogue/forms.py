from oscar.apps.dashboard.catalogue import forms as base_form

from oscar.apps.dashboard.catalogue import forms as base_forms

class ProductForm(base_forms.ProductForm):

    class Meta(base_forms.ProductForm.Meta):

        fields = (
            'title',
            'description'
        )
