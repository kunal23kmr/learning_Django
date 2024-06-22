from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class chaiVerity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="app1s/")
    data_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self) -> str:
        return self.name


# one to many
class chaiReview(models.Model):
    chai = models.ForeignKey(
        chaiVerity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    comment = models.TextField()
    date_review = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.user.username} review for {self.chai.name}'


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(chaiVerity, related_name="stores")

    def __str__(self) -> str:
        return self.name


class chaiCertificate(models.Model):
    chai = models.OneToOneField(
        chaiVerity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_till = models.DateTimeField()

    def __str__(self) -> str:
        return f'certificate for {self.name.chai}'
