from django.shortcuts import render
from .models import chaiVerity
from django.shortcuts import get_object_or_404

# Create your views here.


def all_chai(req):
    chais = chaiVerity.objects.all()
    return render(req, 'app1/all_chai.html', {'chais': chais})


def chai_detail(req, chai_id):
    chai = get_object_or_404(chaiVerity, pk=chai_id)
    return render(req, 'app1/chai_detail.html', {'chai': chai})
