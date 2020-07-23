from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import List


@login_required
def home(request):
    return render(request, 'index.html', {
        'lists': request.user.lists.all()
    })


@login_required
def list_detail(request, list_id):
    user_list = get_object_or_404(List, id=list_id)
    return render(request, 'detail.html', {
        'list': user_list
    })
