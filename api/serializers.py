
from dataclasses import fields
from rest_framework import serializers
from book.models import Book
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class BookSerializer(serializers.ModelSerializer):

    ## Relations in serializer
    def get_author_name(self, obj):
        return obj.author.first_name + " " + obj.author.last_name   
    author_name = serializers.SerializerMethodField("get_author_name")

    class Meta:
        model = Book
        fields = '__all__'
        # exclude = ('id', 'genre')
        # fields = ('id', 'title', 'summary')

    ## Serializer validation
    def validate_title(self, value):
        filter_list = ['javascript', 'laravel', 'PHP']
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError('Dont use {} title'.format(i))
        return value
 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model = User
        model = get_user_model()
        fields = '__all__'
        # exclude = ('id', 'genre')
        # fields = ('title', 'summary')