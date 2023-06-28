from django.db import models

class Ticker(models.Model):
    message = models.TextField(verbose_name="Текст")
    duration = models.IntegerField(verbose_name="Длительность")
    bg_color = models.CharField(max_length=50, verbose_name="Цвет заднего фона")
    text_color = models.CharField(max_length=50, verbose_name="Цвет текста")
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name = 'Бегущая строка'