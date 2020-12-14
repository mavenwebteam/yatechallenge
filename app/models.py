from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Genre(MPTTModel):
	name = models.CharField(max_length=255, unique=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	class MPTTMeta:
		order_insertion_by = ['name']

	def __str__(self):
		full_path = [self.name]
		k = self.parent
		while k is not None:
			full_path.append(k.name)
			k = k.parent
		return ' -> '.join(full_path[::-1])

class Post(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey('Genre', on_delete=models.CASCADE,null=True, blank=True)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False,auto_now_add=False,)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]