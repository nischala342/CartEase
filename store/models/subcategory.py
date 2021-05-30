from django.db import models
class SubCategory(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_subcategories(category_id):
        return SubCategory.objects.filter()

    def __str__(self):
        return self.name
