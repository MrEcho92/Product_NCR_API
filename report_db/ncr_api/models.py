from django.db import models

# Create your models here.
STATUS = ((0, 'Open'), (1, 'Closed'))

class ProductNCR(models.Model):
    customer = models.CharField(max_length=50, null=False)
    product_name = models.CharField(max_length=50, null=False)
    return_ref = models.IntegerField()
    issue = models.CharField(max_length=100, null=False)
    root_cause = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_date = models.DateTimeField(auto_now_add=True)  #time when instance is created

    def __str__(self):
        return 'Ref_00{} for {}'.format(self.id, self.customer)

    class Meta:
        verbose_name = ('Product NCR')
        ordering = ['-id']
