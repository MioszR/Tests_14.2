import tmbd_client
from unittest.mock import Mock

def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmbd_client.requests.get", requests_mock)


   movies_list = tmbd_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_movies_list_type_popular():
    movies_list = tmbd_client.get_movies_list(list_type="popular")
    assert movies_list is not None

def test_get_single_movie(monkeypatch):
    mock_movie = 'Movie1'
    call_tmbd_api_mock = Mock()
    call_tmbd_api_mock.return_value = mock_movie
    monkeypatch.setattr('tmbd_client.call_tmbd_api', call_tmbd_api_mock)
    movie = tmbd_client.get_single_movie(movie_id = 1)
    assert movie == mock_movie

def test_get_single_movie_cast(monkeypatch):
    mock_movie_cast = {'Id': 1, 'cast': [1, 2]}
    call_tmbd_api_mock = Mock()
    call_tmbd_api_mock.return_value = mock_movie_cast
    monkeypatch.setattr("tmbd_client.call_tmbd_api", call_tmbd_api_mock)
    movie_cast = tmbd_client.get_single_movie_cast(movie_id=2)
    return movie_cast == mock_movie_cast

def test_get_movie_images(monkeypatch):
   mock_image = ["Image"]
   call_tmbd_api_mock = Mock()
   call_tmbd_api_mock.return_value = mock_image
   monkeypatch.setattr("tmbd_client.call_tmbd_api", call_tmbd_api_mock)
   movie_image = tmbd_client.get_movie_images(movie_id = 1)
   assert movie_image == mock_image
