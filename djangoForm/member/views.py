from django.shortcuts import render, redirect
from .models import Member
from .forms import AddMemberForm

def Add(request):
    # context = {}
    if request.POST:
        form = AddMemberForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('member-page')
    else:
        form = AddMemberForm()
    return render(request, 'member/home.html', {'form': form})

def Info(request):
    context = {}
    return render(request, 'member/info.html', context)

