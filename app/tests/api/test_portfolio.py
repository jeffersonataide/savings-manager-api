from app.tests.utils.portfolios import create_portfolio


class TestPortfolioApi:
    def test_create_portfolio(self, client, jwt):
        response = create_portfolio(client, jwt, "Stocks")

        assert response.status_code == 201
        assert response.json() == {
            "id": 1,
            "name": "Stocks",
            "user_id": 1,
            "assets": [],
        }

    def test_get_portfolio(self, client, jwt):
        create_portfolio(client, jwt, "Stocks")
        response = client.get(
            "/portfolios/1",
            headers={"Authorization": f"Bearer {jwt}"},
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": "Stocks",
            "user_id": 1,
            "assets": None,
        }

    def test_list_portfolios(self, client, jwt):
        create_portfolio(client, jwt, "Stocks")
        response = client.get(
            "/portfolios",
            headers={"Authorization": f"Bearer {jwt}"},
        )
        assert response.status_code == 200
        assert response.json() == [
            {"id": 1, "name": "Stocks", "user_id": 1, "assets": None}
        ]

    def test_update_portfolio(self, client, jwt):
        create_portfolio(client, jwt, "Stocks")
        response = client.put(
            "/portfolios/1",
            json={"name": "Savings"},
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": "Savings",
            "user_id": 1,
            "assets": [],
        }

    def test_delete_portfolio(self, client, jwt):
        create_portfolio(client, jwt, "Stocks")
        response = client.delete(
            "/portfolios/1",
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": "Stocks",
            "user_id": 1,
            "assets": [],
        }
