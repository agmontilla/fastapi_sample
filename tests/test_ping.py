from fastapi.testclient import TestClient
from http import HTTPStatus


class TestPing:

    ENDPOINT = "/ping"

    def test_ping_endpoint_is_working(cls, client: TestClient) -> None:
        response = client.get(cls.ENDPOINT)
        assert response.status_code == HTTPStatus.OK
        assert response.json() == "pong!"
