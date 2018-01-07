import pytest
import json

from documenters_aggregator.spiders.ccbc import CcbcSpider


test_response = []
with open('tests/files/ccbc.txt') as f:
    for line in f:
        test_response.append(json.loads(line))
spider = CcbcSpider()
parsed_items = [item for item in spider._parse_events(test_response)]


def test_name():
    assert parsed_items[25]['name'] == 'Board of Commissioners'


def test_description():
    expected_description = ('https://cook-county.legistar.com/'
                            'View.ashx?M=A&ID=521583&GUID=EA23CB0D'
                            '-2E10-47EA-B4E2-EC7BA3CB8D76')
    assert parsed_items[25]['description'] == expected_description


def test_start_time():
    assert parsed_items[25]['start_time'] == '2017-09-13T11:00:00-05:00'


@pytest.mark.parametrize('item', parsed_items)
def test_end_time(item):
    assert item['end_time'] is None


def test_id():
    assert parsed_items[25]['id'] == 'BoardofCommissioners9132017'


@pytest.mark.parametrize('item', parsed_items)
def test_all_day(item):
    assert item['all_day'] is False


@pytest.mark.parametrize('item', parsed_items)
def test_classification(item):
    assert item['classification'] == 'Not classified'


def test_status():
    assert parsed_items[25]['status'] == 'passed'


def test_location():
    assert parsed_items[25]['location'] == {
        'url': None,
        'name': 'Cook County Building, Board Room, 118 North Clark Street, Chicago, Illinois',
        'coordinates': {
            'latitude': None,
            'longitude': None,
        },
    }


@pytest.mark.parametrize('item', parsed_items)
def test__type(item):
    assert parsed_items[0]['_type'] == 'event'
