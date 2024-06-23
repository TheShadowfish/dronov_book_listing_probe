from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Bb(models.Model):
    BUY = 'b'
    SELL = 's'
    EXCHANGE = 'c'

    KINDS = (
        (None, 'Выберите тип публикуемого объявления'),
        ('Купля-продажа', (
            (BUY, 'Куплю'),
            (SELL, 'Продам'),
        )),
        ('Обмен', (
            (EXCHANGE, 'Обменяю'),
        ))
    )
    """
    class Kinds(models.TextChoices):
        BUY = 'b', 'Куплю'
        SELL = 's', 'Продам'
        EXCHANGE = 'c', 'Обменяю'
        RENT = 'r'
        __empty__ = 'Выберите тип публикуемого объявления'
        
    kind = models.CharField(max_length=1, choices=Kinds.choices, default=Kinds.SELL)
    
    
    class Kinds(models.IntegerChoices):
        BUY = 1, 'Куплю'
        SELL = 2, 'Продам'
        EXCHANGE = 3, 'Обменяю'
        RENT = 4
        
    kind = models.SmallIntegerField(choices=Kinds.choices, default=Kinds.SELL)
    """
    kind = models.CharField(max_length=1, choices=KINDS, blank=True)

    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(**NULLABLE, verbose_name='Описание')
    price = models.FloatField(**NULLABLE, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

    def __str__(self):
        return f"{self.title} - {self.published}"


class Rubric (models .Model) :
    name = models.CharField(max_length=20, db_index=True,  verbose_name='Название рубрики')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
