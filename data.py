import requests


parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
question_data = []


def fetch_and_set_questions() -> None:
    ''' Update questions data by fetching from opentdb API. '''
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    # Raise exeception for response code other than 200
    response.raise_for_status()
    global question_data
    question_data = response.json()['results']


fetch_and_set_questions()
