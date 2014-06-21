from django.contrib.sitemaps import Sitemap

class MainSitemap(Sitemap) :

	def items(self):
		return [self]

	location = "/"
	changefreq="monthly"
	priority = "1"

class ProfileSitemap(Sitemap):
	def items(self):
		return [self]

	location = "/profile"
	changefreq = "monthly"
	priority = "1"

class AreasSitemap(Sitemap):
	def items(self):
		return [self]

	location = "/areas"
	changefreq = "monthly"
	priority = "1"

class DirectionsSitemap(Sitemap):
	def items(self):
		return [self]

	location = "/directions"
	changefreq = "monthly"
	priority = "1"

class ContactSitemap(Sitemap):
	def items(self):
		return [self]

	location = "/contact"
	changefreq = "monthly"
	priority = "1"


sitemaps = {
	'/': MainSitemap,
	'/profile': ProfileSitemap,
	'/areas': AreasSitemap,
	'/directions': DirectionsSitemap,
	'/contact': ContactSitemap,
}