from django.contrib import admin
from .models import Faq

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'question_category', 'answer', 'generators', 'created_at', 'last_modifier', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')