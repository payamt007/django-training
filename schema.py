import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene import Field, List, ObjectType
from prgraph.models import Category, Ingredient
from prgraph.forms import SignUpForm
from prgraph import schema as prgraph_schema

# mxing all Queries and Mutations from different modules


class Mutation(prgraph_schema.Mutation, graphene.ObjectType):
    pass


class Query(prgraph_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
