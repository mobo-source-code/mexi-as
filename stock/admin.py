from django.contrib import admin
from .models import Article, Taking, TakingArticles, Feeding, Fournisseur, FeedingArticles

# Register your models here.

admin.site.register(Article)
admin.site.register(Taking)
admin.site.register(TakingArticles)
admin.site.register(Feeding)
admin.site.register(FeedingArticles)
admin.site.register(Fournisseur)

