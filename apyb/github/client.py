from gql import Client
from gql.transport.httpx import HTTPXTransport

GITHUB_GRAPHQL_ENDPOINT = "https://api.github.com/graphql"


def get_github_client(token: str):
    transport = HTTPXTransport(
        url=GITHUB_GRAPHQL_ENDPOINT,
        headers={
            "Authorization": f"Bearer {token}",
        },
    )
    return Client(transport=transport, fetch_schema_from_transport=True)
