from django.shortcuts import render, redirect
from .models import Index, Educations, Experience, Skill, Dasturlash, Awards, Blog, Single
from .forms import ContactForm, CommentForm


# Create your views here.
def index(request):
    indexx = Index.objects.all()
    edu = Educations.objects.all()
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    dasturlaash = Dasturlash.objects.all()
    awards = Awards.objects.all()
    blog = Blog.objects.all()
    contact = ContactForm(request.POST or None)
    if contact.is_valid():
        contact.save()
        return redirect('.')
    context = {
        'index': indexx,
        'education': edu,
        'experience': experience,
        'skill': skill,
        'dasturlash': dasturlaash,
        'awards': awards,
        'our_blog': blog,
        'contact': contact,

    }
    return render(request, 'index.html', context)


def single(request):
    single = Single.objects.all()
    blog = Blog.objects.all()
    comment = CommentForm(request.POST or None,)
    if comment.is_valid():
        com = comment.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')
    cnt = {
        'single': single,
        'cmt': comment,
    }
    return render(request, 'single.html', cnt)
