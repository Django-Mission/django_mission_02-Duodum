from django.contrib import admin
from .models import Inquiry, Answer

class AnswerInlines(admin.TabularInline):
    model = Answer
    extra = 1
    min_num = 0
    max_num = 1
    verbose_name = '답변'
    verbose_name_plural = '답변'
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_category', 'title', 'e_mail', 'e_mail_checkbox', 'text_message', 'text_message_checkbox', 
        'content', 'generators', 'created_at', 'last_modifier', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    inlines = [AnswerInlines]