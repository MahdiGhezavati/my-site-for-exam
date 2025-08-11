from django.contrib.sitemaps import Sitemap
from Artwork.models import Artwork


class ArtworkSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Artwork.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.poblished_date