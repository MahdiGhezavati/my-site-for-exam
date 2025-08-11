from django.contrib.sitemaps import Sitemap
from Artist.models import Artist


class ArtistSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Artist.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.poblished_date