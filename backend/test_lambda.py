import json
import pytest
from unittest.mock import patch, MagicMock
from lambda_function import lambda_handler
@pytest.fixture
def mock_table():
    with patch('lambda_function.boto3') as mock:
        mock_table = MagicMock()
        mock.resource.return_value.Table.return_value = mock_table
        mock_table.update_item.return_value = {
            'Attributes': {
                'count': 5
            }
        }
        yield mock
def test_returns_200(mock_table):
    response = lambda_handler({},{})
    assert response['statusCode'] == 200
def test_returns_cors_header(mock_table):
    response = lambda_handler({},{})
    assert response['headers']['Access-Control-Allow-Origin'] == '*'
def test_returns_count(mock_table):
    response = lambda_handler({},{})
    body = json.loads(response['body'])
    assert 'count' in body
def test_count_is_number(mock_table):
    response = lambda_handler({},{})
    body = json.loads(response['body'])
    assert isinstance(body['count'], int)
