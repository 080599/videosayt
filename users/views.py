from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from content.models import Video, User, Comment
from .forms import VideoForm, LoginForm, RegisterForm, CommentForm

def home(request):
    videos = Video.objects.all().order_by('-created_at')
    context = {'videos': videos}
    return render(request, 'home.html', context)

def video_detail(request, video_id):
    video = Video.objects.get(pk=video_id)
    comments = Comment.objects.filter(video=video).order_by('-created_at')
    comment_form = CommentForm()
    context = {'video': video, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'video_detail.html', context)

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    context = {'form': form}
    return render(request, 'upload_video.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def add_comment(request, video_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_user = request.user
            comment.video_id = video_id
            comment.save()
            return redirect('video_detail', video_id=video_id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'add_comment.html', context)

def like_video(request, video_id):
    video = Video.objects.get(pk=video_id)
    video.like += 1
    video.save()
    return redirect('video_detail', video_id=video_id)

def dislike_video(request, video_id):
    video = Video.objects.get(pk=video_id)
    video.dislike += 1
    video.save()
    return redirect('video_detail', video_id=video_id)