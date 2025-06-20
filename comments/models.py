from django.db import models
from auth_user.models import User
from news_board.models import News

class Comment(models.Model):
    '''Модель комментариев'''
    news_id = models.ForeignKey(News,
                                to_field='id',
                                on_delete=models.CASCADE,
                                null=False)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User,
                        on_delete=models.CASCADE,
                        null=False)

    class Meta():
        db_table='comment'

    def __str__(self):
        return self.content
