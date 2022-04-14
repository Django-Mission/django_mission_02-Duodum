from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Faq(models.Model):
    GENERAL = 'GE'
    ACCOUNT = 'AC'
    ETC = 'ET'

    CATEGORY_CHOICES = [
        (GENERAL, '일반'),
        (ACCOUNT, '계정'),
        (ETC, '기타'),
    ]

    question = models.CharField(
        '질문',
        max_length=100,
    )

    question_category = models.CharField(
        '카테고리',
        max_length = 2,
        choices = CATEGORY_CHOICES,
        default = GENERAL,
    )

    answer = models.TextField('답변')
    generators = models.ForeignKey(User, models.CASCADE, related_name='generators_faq')
    created_at = models.DateTimeField('생성일시', auto_now_add=True)
    last_modifier = models.ForeignKey(User, models.CASCADE, null=True, blank=True, related_name='last_modifier_faq')
    updated_at = models.DateTimeField('수정일시', auto_now=True)