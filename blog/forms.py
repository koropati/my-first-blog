from django import forms
from .models import Post, Jurnal

class PostForm(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta:
		model = Post
		fields = ('title','text',)

class JurnalForm(forms.ModelForm):
	"""docstring for JurnalForm"""
	class Meta:
		model = Jurnal
		fields = ('judul','penulis','tahun','sensor','algoritma','penerapan',)
		