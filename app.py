from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema, Int, Field, List, Mutation

items = []

class ItemType(ObjectType):
    id = Int()
    name = String()
    description = String()

class Query(ObjectType):
    items = List(ItemType)
    item = Field(ItemType, id=Int())

    def resolve_items(root, info):
        return items

    def resolve_item(root, info, id):
        return next((i for i in items if i['id'] == id), None)

class CreateItem(Mutation):
    class Arguments:
        name = String()
        description = String()

    item = Field(lambda: ItemType)

    def mutate(self, info, name, description):
        item = {'id': len(items)+1, 'name': name, 'description': description}
        items.append(item)
        return CreateItem(item=item)

class Mutation(ObjectType):
    create_item = CreateItem.Field()

schema = Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql', schema=schema, graphiql=True))