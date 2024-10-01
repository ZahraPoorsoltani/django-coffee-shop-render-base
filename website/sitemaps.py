from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class WebsiteStaticSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return ['website:index']

    def location(self, item):
        return reverse(item)