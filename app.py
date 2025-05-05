from flask import Flask, request, jsonify
from graphene import ObjectType, String, Schema, Int, Boolean, Field, List, Mutation
from flask_graphql import GraphQLView
from models import guitars  # Importar datos desde models.py

class GuitarType(ObjectType):
    id = Int()
    name = String()
    image = String()
    description = String()
    price = Int()
    stock = Int()
    available = Boolean()

class Query(ObjectType):
    guitars = List(GuitarType)
    guitar = Field(GuitarType, id=Int(required=True))

    def resolve_guitars(root, info):
        return guitars

    def resolve_guitar(root, info, id):
        return next((g for g in guitars if g["id"] == id), None)


class UpdateStock(Mutation):
    class Arguments:
        id = Int(required=True)
        quantity = Int(required=True)

    guitar = Field(lambda: GuitarType)

    def mutate(self, info, id, quantity):
        guitar = next((g for g in guitars if g["id"] == id), None)
        if guitar:
            guitar["stock"] = max(guitar["stock"] - quantity, 0)
            guitar["available"] = guitar["stock"] > 0
            return UpdateStock(guitar=guitar)
        return UpdateStock(guitar=None)


class Mutation(ObjectType):
    update_stock = UpdateStock.Field()


schema = Schema(query=Query, mutation=Mutation)


app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Esto habilita la interfaz visual
    )
)


if __name__ == '__main__':
    app.run(debug=True)
