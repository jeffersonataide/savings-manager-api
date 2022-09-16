from app.tests.utils.portfolios import create_portfolio
from app.tests.utils.assets import create_asset


class TestAssetApi:
    def test_create_asset(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")

        response = create_asset(client, jwt, "Savings", 1)

        assert response.status_code == 201
        assert response.json() == {"id": 1, "name": "Savings", "portfolio_id": 1}
