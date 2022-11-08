from django.conf import settings
from django.db import models
from django.utils import timezone

class Post (models.Model):#models.Model Post'un bir django modeli oldugunu belirtir bu şekilde onu db'de tutması gerektiğini bilir.
    # postta olması gereken features ;
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #başka bir modele referans tanımlar
    title = models.CharField(max_length=200) #belirli bir uzunluktaki metinleri tanımlamak için kullanılır.
    text = models.TextField() #bu da uzun metinleri tanımlar
    created_date = models.DateTimeField(default=timezone.now) #gün ve saati tanımlama
    published_date = models.DateTimeField(blank=True,null=True)

    #def'ler nesnenin yaptıkları methods yani
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  #__dunder (double underscore)
        return self.title


