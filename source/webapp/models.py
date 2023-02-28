from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


# Create your models here.

class CategoryChoice(TextChoices):
    OTHER = 'OTHER', 'Разное'
    NOTEBOOKS = 'NOTEBOOKS', 'Ноутбуки'
    CARS = 'CARS', 'Машины'
    BOARD_GAME = 'BOARD_GAME', 'Настольные игры'
    CHEMISTRY = 'Chemistry', 'Химия'


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=False, verbose_name='Описание')
    image = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Картинка')
    category = models.TextField(max_length=1000, null=False, verbose_name='Категория',
                                choices=CategoryChoice.choices, default=CategoryChoice.OTHER)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')
    remainder = models.PositiveIntegerField(default=0)
    is_deleted = models.BooleanField(verbose_name='Удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def __str__(self):
        return f'{self.name}-{self.description}-{self.image}-{self.category}-{self.price}-{self.remainder}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()