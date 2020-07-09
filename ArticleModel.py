
from django.db import models

from DataManagerApplication.models import UserModel

class ArticleModel(models.Model):
	
	uploaded_by = models.OneToOneField(
	UserModel,
	on_delete = models.PROTECT,
	verbose_name = 'Uploaded by the ',
	primary_key = False)
	
	title = models.TextField(
	'Title of an Article',
	max_length = 1000,
	)
	
	description = models.TextField(
	'Description of an Article',
	max_length = 4000,
	)
	
	author = models.CharField(
	'Author of this Article',
	max_length = 100,
	blank = False)
	
	published_on = models.DateField(
	'Published on the Date',
	auto_now = False)
	
	published_by = models.TextField(
	'Published by the ',
	max_length = 1000,
	blank = True)
	
	document = models.FileField(
	'Document of the Article',
	upload_to = f'StaticFolder/Uploads/Documents/Articles/{title}/',name='Document.txt',
	blank = False,
	help_text = 'Url Configuration of the Article')
	
	related_domains = models.ManyToManyField(
	Domain,
	verbose_name = 'Related Fields')
	
	download_option = models.BooleanField(
	'Available For Download',
	default = True)
	
	def __str__(self):
		return self.title
		
		
		

		
	