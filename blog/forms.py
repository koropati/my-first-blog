from django import forms
from .models import Post, Jurnal, Data

class PostForm(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta:
		model = Post
		fields = ('title','text',)
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Judul Postingan'}),
			'text': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Isi Postingan'}),
		}

class JurnalForm(forms.ModelForm):
	"""docstring for JurnalForm"""
	class Meta:
		model = Jurnal
		fields = ('judul','penulis','tahun','sensor','algoritma','penerapan',)
		widgets = {
			'judul': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Judul Jurnal'}),
			'penulis': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Penulis'}),
			'tahun': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD', 'readonly':'readonly', 'id':'departure1'}),
			'sensor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Jenis Sensor'}),
			'algoritma': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Algoritma'}),
			'penerapan': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tempat Penerapan'}),
		}

class DataForm(forms.ModelForm):
	class Meta:
		model = Data
		fields = ('data',)
		widgets = {
			'data' : forms.TextInput(),
		}