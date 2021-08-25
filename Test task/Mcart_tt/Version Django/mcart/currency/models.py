from django.db import models


class exchRate_models(models.Model):
    symbolCod_curr = models.CharField('Символьный код валюты', max_length=5)    # yes
    amountCur = models.IntegerField('Количество валюты')                        # вроде
    date_to = models.DateField('Начальная дата')                                # yes
    size_to = models.TextField('Размер валюты в начальную дату')               # вроде
    date_from = models.DateField('Конечная дата')                               # yes
    size_from = models.TextField('Размер валюты в конечную дату')              # вроде
    difference = models.FloatField('Разница в ₽')                               # вроде

    def __str__(self):
        return self.symbolCod_curr
