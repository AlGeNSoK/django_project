from django.contrib import admin

from django.core.exceptions import ValidationError

from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class RelationshipInlineFormSet(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                i += 1
            else:
                continue
        if i == 0:
            raise ValidationError('Укажите основной раздел')
        elif i > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class TagsTitleInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormSet


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsTitleInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
