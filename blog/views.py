from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Jurnal
from .forms import PostForm, JurnalForm
# Create your views here.
@login_required
def dashboard(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	jurnals = Jurnal.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'blog/dashboard.html', {'posts' : posts, 'jurnals' : jurnals})

@login_required
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts' : posts})

@login_required
def jurnal_list(request):
 	jurnals = Jurnal.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
 	return render(request,'blog/jurnal_list.html', {'jurnals' : jurnals})

@login_required
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post' : post})

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			# post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form' : form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html',{'posts':posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list');

@login_required
def jurnal_new(request):
 	if request.method == "POST":
 		form = JurnalForm(request.POST)
 		if form.is_valid():
 			jurnal = form.save(commit=False)
 			jurnal.author = request.user
 			jurnal.created_date = timezone.now()
 			jurnal.save()
 			return redirect('jurnal_list')
 	else:
 		form = JurnalForm()
 		return render(request, 'blog/jurnal_edit.html', {'form' : form})

@login_required
def jurnal_edit(request, pk):
    jurnal = get_object_or_404(Jurnal, pk=pk)
    if request.method == "POST":
        form = JurnalForm(request.POST, instance=jurnal)
        if form.is_valid():
            jurnal = form.save(commit=False)
            jurnal.author = request.user
            jurnal.created_date = timezone.now()
            jurnal.save()
            return redirect('jurnal_list')
    else:
        form = JurnalForm(instance=jurnal)
    return render(request, 'blog/jurnal_edit.html', {'form': form})