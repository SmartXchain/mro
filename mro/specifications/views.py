from django.shortcuts import render, get_object_or_404
from .models import Spec

def spec_list(request):
    specs = Spec.published.all()
    return render(request, 'specifications/spec_list.html', {'specs': specs})

def spec_detail(request, id):
    spec = get_object_or_404(Spec, id=id, status=Spec.Status.PUBLISHED)
    return render(request, 'specifications/spec_detail.html', {'spec':spec})