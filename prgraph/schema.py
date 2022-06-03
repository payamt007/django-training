import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene import Field, List, ObjectType
from prgraph.models import Category, Ingredient
from prgraph.forms import SignUpForm
from graphene_django.rest_framework.mutation import SerializerMutation

from prgraph.serializers import CategorySerializer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")


class CategoryMutation(DjangoModelFormMutation):
    nm = Field(CategoryType)
    class Meta:
        form_class = SignUpForm


class MyFirstDRFMutation(SerializerMutation):
    class Meta:
        serializer_class = CategorySerializer
        model_operations = ['update', 'create', 'delete']
        lookup_field = 'id'

class Mutation(ObjectType):
    create_category = CategoryMutation.Field()
    update_category = MyFirstDRFMutation.Field()


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(
        CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None






