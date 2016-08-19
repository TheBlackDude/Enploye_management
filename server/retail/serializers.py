from rest_framework import serializers
from .models import Chain, Store, Employee

class ChainSerializer(serializers.ModelSerializer):
    """ serializer to represent the chain model. """

    class Meta:
        model = Chain
        fields = (
                  "name", "description", "slogan", "founded_date",
                  "website")


class StoreSerializer(serializers.ModelSerializer):
    """ Serializer to represent the store model. """

    class Meta:
        model = Store
        fields = (
                 "chain", "number", "address", "opening_date",
                 "business_hours_start", "business_hours_end"
            )



class EmployeeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model. """

    class Meta:
        model = Employee
        fields = ("store", "number", "first_name", "last_name",
                  "hired_date")
