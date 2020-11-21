from .models import ProductNCR
from rest_framework import serializers

class ProductNCRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductNCR
        fields = ('id','customer', 'product_name', 'return_ref', 'issue', 'root_cause', 'status', 'created_date')
