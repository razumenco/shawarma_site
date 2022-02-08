from django.shortcuts import render, get_object_or_404

from .models import Shawarma, Review
from .models import ReviewForm

def shawarma_list(request):
    shawarmas = Shawarma.objects.all()
    return render(request, "shawarma_app/shawarmas.html", context={"shawarmas":shawarmas})


def shawarma_detail(request, id):
    shawarma = get_object_or_404(Shawarma, pk=id)
    reviews = Review.objects.filter(about__id=id)
    if len(reviews) > 0:
        rating = sum([review.mark for review in reviews]) / len(reviews)
    else:
        rating = 0
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "shawarma_app/detail.html", context={'shawarma':shawarma, 'reviews':reviews, 'rating':rating, 'form': form})


def about(request):
    return render(request, "shawarma_app/about.html")

