import pytest
from schema import Or, Schema


@pytest.fixture
def post_detail_data():
    return {"id": int, "title": str, "content": str, "created_at": str}


@pytest.fixture
def post_detail_schema(post_detail_data):
    schema = Schema(post_detail_data)
    return schema


@pytest.fixture
def post_list_schema(post_detail_data):
    post_list_data = {"author": {"username": str, "email": str}}
    post_list_data.update(post_detail_data)
    schema = Schema(
        {
            "count": int,
            "next": Or(str, None),
            "previous": Or(str, None),
            "results": [post_list_data],
        }
    )
    return schema
