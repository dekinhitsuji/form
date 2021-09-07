from django.db import models

#モデルクラスを定義
class People(models.Model):
    Name = models.CharField(max_length=100)
    Furigana = models.CharField(max_length=100)
    Tell = models.IntegerField(blank=True, null=True)
    Mail = models.EmailField(max_length=100)
    Birthday = models.CharField(max_length=20)
    Adress = models.CharField(max_length=100)
