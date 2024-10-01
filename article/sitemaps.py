from django.contrib.sitemaps import Sitemap
from .models import Post
from django.utils import timezone


class ArticleSitemap(Sitemap):
    changefreq = "weakly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status =1,published_date__lte= timezone.now())

    def lastmod(self, obj):
        return obj.published_date