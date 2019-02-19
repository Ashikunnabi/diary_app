from django.forms import ModelForm
from .models import Story

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : "What('s') on your mind?"})