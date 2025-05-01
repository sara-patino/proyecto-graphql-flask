# schema.py

import graphene
from models import guitars

class Guitar(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    precio = graphene.Float()
    stock = graphene.Int()
    disponible = graphene.Boolean()

class Query(graphene.ObjectType):
    all_guitars = graphene.List(Guitar)

    def resolve_all_guitars(root, info):
        return guitars

class UpdateStock(graphene.Mutation):
    class Arguments:
        guitar_id = graphene.Int(required=True)
        amount = graphene.Int(required=True)

    guitar = graphene.Field(lambda: Guitar)

    def mutate(root, info, guitar_id, amount):
        for p in guitars:
            if p["id"] == guitar_id:
                p["stock"] += amount
                if p["stock"] <= 0:
                    p["stock"] = 0
                    p["disponible"] = False
                else:
                    p["disponible"] = True
                return UpdateStock(guitar=p)
        raise Exception("Producto no encontrado")

class Mutation(graphene.ObjectType):
    update_stock = UpdateStock.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
