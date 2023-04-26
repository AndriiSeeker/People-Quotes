from django.forms import ModelForm, CharField, TextInput, ModelMultipleChoiceField, ModelChoiceField, Select, \
    SelectMultiple
from .models import Quote, Author, Tag


class QuoteForm(ModelForm):
    quote = CharField(min_length=5, widget=TextInput(), required=True)
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by("name"),
                                    widget=SelectMultiple(), required=True)
    author = ModelChoiceField(queryset=Author.objects.all().order_by("fullname"),
                              widget=Select(), required=True)

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput())
    born_date = CharField(max_length=50, widget=TextInput())
    born_location = CharField(max_length=150, widget=TextInput())
    description = CharField(widget=TextInput())

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class TagForm(ModelForm):
    name = CharField(max_length=50, widget=TextInput())

    class Meta:
        model = Tag
        fields = ["name"]