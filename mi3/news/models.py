from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=60)
    annons = models.CharField('Анонс', max_length=250)
    # image = models.ImageField(null=True, blank=True, upload_to="images/")
    text = models.TextField('Статья')
    post_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
