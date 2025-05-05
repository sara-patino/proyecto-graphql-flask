import unittest
from app import app, schema
from models import guitars


class GraphQLTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.url = "/graphql"

    def post_query(self, query):
        return self.client.post(self.url, json={"query": query})

    def test_guitars_query(self):
        query = '''
        {
            guitars {
                id
                name
            }
        }
        '''
        response = self.post_query(query)
        data = response.get_json()
        self.assertIn("guitars", data["data"])
        self.assertTrue(len(data["data"]["guitars"]) > 0)

    def test_single_guitar_query(self):
        query = '''
        {
            guitar(id: 1) {
                id
                name
                stock
                available
            }
        }
        '''
        response = self.post_query(query)
        data = response.get_json()
        self.assertEqual(data["data"]["guitar"]["id"], 1)

    def test_update_stock_mutation(self):
        # Reset guitar for consistency
        guitars[0]["stock"] = 2
        guitars[0]["available"] = True

        mutation = '''
        mutation {
            updateStock(id: 1, quantity: 2) {
                guitar {
                    id
                    stock
                    available
                }
            }
        }
        '''
        response = self.post_query(mutation)
        data = response.get_json()
        updated_guitar = data["data"]["updateStock"]["guitar"]
        self.assertEqual(updated_guitar["stock"], 0)
        self.assertFalse(updated_guitar["available"])


if __name__ == "__main__":
    unittest.main()
