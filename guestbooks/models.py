from django.db import models
from accounts.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True

class GuestBook(BaseModel):
    title = models.CharField(verbose_name="제목", max_length=30)
    content = models.TextField(verbose_name="내용")
    writer = models.CharField(verbose_name="작성자", max_length=30)
    password = models.TextField(verbose_name="비밀번호")
