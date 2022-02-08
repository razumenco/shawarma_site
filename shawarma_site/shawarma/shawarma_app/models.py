from django.db import models
from django.forms import ModelForm


class Shawarma(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    start_time = models.TimeField()
    stop_time = models.TimeField()
    working_status = models.CharField(max_length=50)
    location_iframe = models.TextField()
    main_image = models.ImageField()
    standart_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Review(models.Model):
    about = models.ForeignKey(Shawarma, on_delete=models.CASCADE)
    mark_choice = [
        (1, "Мерзко"),
        (2, "Невкусно"),
        (3, "Нормально"),
        (4, "Вкусно"),
        (5, "Очень вкусно")
    ]
    mark = models.PositiveIntegerField(choices=mark_choice)
    comment = models.TextField()


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['mark', 'comment']
