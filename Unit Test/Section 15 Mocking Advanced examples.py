

# Exercise 1
# Suppose you have the function that sends an HTTP GET request and retries up to 3 times:


# import requests
# import time

# def get_content(url):
#     for attempt in range(3):
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#             return response.content.decode("utf-8")
#         except Exception:
#             time.sleep(1)
#     raise Exception(f"Failed to get content from {url}")


# This function takes a URL as input, and uses a for loop to retry the request up to 3 times. It uses the requests.get() function to send an HTTP GET request to the given URL, and raises an exception if the response status code indicates an error (using the raise_for_status() method). It then decodes the response content using UTF-8 encoding, and returns it as a string. If the request fails after 3 attempts, it raises an exception with a message indicating the failure.


# Define a class called TestGetContent that inherits from unittest.TestCase. Write the unit tests using the unittest framework and the unittest.mock library to mock the requests library.


# You should use the patch decorator from the unittest.mock library to mock the requests.get() function. Define two test cases, one for a successful request and one for a request that fails and needs to be retried:

# test_success()

# test_retry()


# In the successful request test case, create a MagicMock object to represent the response from the requests.get() function, and set its status code, content, and return value. Then call the get_content() function with a URL, and use the assertEqual() method to check that the result is the expected string, and the assert_called_once_with() method to check that the requests.get() function was called once with the correct URL.


# In the retry test case, set up the requests.get() function to raise an exception on the first two attempts, and return a MagicMock object representing a successful response on the third attempt. Then call the get_content() function with a URL, and use the assertEqual() method to check that the result is the expected string, and the assertEqual() to check that the requests.get() function was called three times.


# Solution 1
import unittest
from unittest.mock import MagicMock, patch
from my_module import get_content


class TestGetContent(unittest.TestCase):
    @patch("requests.get")
    def test_success(self, mock_get):
        mock_response = MagicMock(
            status_code=200, content=b"Hello, world!"
        )
        mock_get.return_value = mock_response

        result = get_content("http://example.com")

        self.assertEqual(result, "Hello, world!")
        mock_get.assert_called_once_with("http://example.com")

    @patch("requests.get")
    def test_retry(self, mock_get):
        mock_response = MagicMock(
            status_code=500, content=b"Hello, world!"
        )
        mock_get.side_effect = [Exception, Exception, mock_response]

        result = get_content("http://example.com")

        self.assertEqual(result, "Hello, world!")
        self.assertEqual(mock_get.call_count, 3)

# ==================================================================================
# Exercise 2
# Suppose you have the function that fetches the current weather data:


# import requests


# def get_weather(location):
#     url = (
#         f"http://api.openweathermap.org/data/2.5/weather"
#         f"?q={location}&appid=<your API key>"
#     )
#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()
#     return {
#         "location": data["name"],
#         "temperature": data["main"]["temp"],
#         "weather_description": data["weather"][0]["description"],
#         "humidity": data["main"]["humidity"],
#     }


# This function takes a location parameter as input, constructs a URL for the OpenWeatherMap API with the location and your API key, and uses the requests.get() function to fetch the weather data. It raises an exception if the response status code indicates an error (using the raise_for_status() method), and parses the response data as JSON using the json method. It then constructs a dictionary containing the location name, temperature, weather description, and humidity from the response data, and returns it.


# Define a class called TestGetWeather that inherits from unittest.TestCase. Write the unit tests using the unittest framework and the unittest.mock library to mock the requests library.


# You should use the patch decorator from the unittest.mock library to mock the requests.get() function.


# Define test case only for a successful API response. In the successful response test case, create a MagicMock object to represent the response from the requests.get() function, and set its status code, JSON data, and return value. Then call the get_weather() function with a location, and use the assertEqual() method to check that the result is a dictionary containing the correct information.


# Solution 2
# import unittest
# from unittest.mock import MagicMock, patch
# from my_module import get_weather


# class TestGetWeather(unittest.TestCase):
#     @patch("requests.get")
#     def test_success(self, mock_get):
#         mock_response = MagicMock()
#         mock_response.status_code = 200
#         mock_response.json.return_value = {
#             "name": "London",
#             "main": {"temp": 283.15, "humidity": 70},
#             "weather": [{"description": "scattered clouds"}],
#         }
#         mock_get.return_value = mock_response

#         result = get_weather("London,UK")

#         self.assertEqual(result["location"], "London")
#         self.assertEqual(result["temperature"], 283.15)
#         self.assertEqual(
#             result["weather_description"], "scattered clouds"
#         )
#         self.assertEqual(result["humidity"], 70)
#         mock_get.assert_called_once_with(
#             "http://api.openweathermap.org/data/2.5/weather"
#             "?q=London,UK&appid=<your API key>"
#         )


# ==================================================================================
# Exercise 3
# Suppose you are building a program that fetches data from an external API and performs some operations on it. You want to write tests for the program using unittest and mocking to ensure that it works as expected.


# You've created a function that fetches data from the API (see my_module.py file):


# import requests


# def fetch_data():
#     response = requests.get('https://example.com/data')
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None


# Next, you've created a function that processes the data (see my_module.py file):


# def get_average_value(data, field):
#     values = [item[field] for item in data if field in item]
#     if len(values) > 0:
#         return sum(values) / len(values)
#     else:
#         return None


# Create a class named TestMyModule that tests these functions using unittest and mocking:

# In the test_fetch_data() method, mock the requests library to return a specific response (for example [{'value': 1}, {'value': 2}, {'value': 3}]). This ensures that the test is not dependent on the external API and that the fetch_data() function works as expected.

# In the test_get_average_value() method, test three different scenarios: valid data, missing field, and no data. This ensures that the get_average_value() function works as expected for different inputs.


# Solution 3
# Sample solution:

# import unittest
# from unittest.mock import MagicMock, patch
# from my_module import fetch_data, get_average_value


# class TestMyModule(unittest.TestCase):
#     def test_fetch_data(self):
#         # Mock the requests library to return a specific response
#         mock_response = MagicMock()
#         mock_response.status_code = 200
#         mock_response.json.return_value = [
#             {"value": 1},
#             {"value": 2},
#             {"value": 3},
#         ]
#         with patch("requests.get", return_value=mock_response):
#             data = fetch_data()
#         self.assertEqual(
#             data, [{"value": 1}, {"value": 2}, {"value": 3}]
#         )

#     def test_get_average_value(self):
#         # Test with valid data
#         data = [{"value": 1}, {"value": 2}, {"value": 3}]
#         field = "value"
#         result = get_average_value(data, field)
#         self.assertEqual(result, 2)

#         # Test with missing field
#         data = [{"value": 1}, {"other_field": 2}, {"value": 3}]
#         field = "value"
#         result = get_average_value(data, field)
#         self.assertEqual(result, 2)

#         # Test with no data
#         data = []
#         field = "value"
#         result = get_average_value(data, field)
#         self.assertIsNone(result)


# ==================================================================================

# Exercise 4
# Let's say you have a class called WeatherAPI that fetches weather data from a third-party API, and a class called WeatherAnalyzer that analyzes the weather data to determine if it's going to rain. Here's the code for the WeatherAPI and WeatherAnalyzer classes:


# import requests


# class WeatherAPI:
#     def __init__(self, api_key):
#         self.api_key = api_key

#     def get_weather(self, city):
#         url = (
#             f"https://api.openweathermap.org/data/2.5/weather"
#             f"?q={city}&appid={self.api_key}"
#         )
#         response = requests.get(url)
#         return response.json()


# class WeatherAnalyzer:
#     def is_raining(self, weather_data):
#         return weather_data["weather"][0]["main"] == "Rain"


# Define a class called TestWeatherAnalyzer that inherits from unittest.TestCase. Write the unit tests using the unittest framework and the unittest.mock library to mock the weather data. In the TestWeatherAnalyzer class define one test case named test_is_raining().


# Create a mock weather data dictionary, for example:


# weather_data = {
#     'weather': [
#         {
#             'main': 'Rain'
#         }
#     ]
# }


# Then, create a mock weather API object using mock.MagicMock.  Specify that the get_weather() method of the mock weather API should return the mock weather data. Create a WeatherAnalyzer instance using the mock weather API, and call the is_raining() method with the city name "London". Then, assert that the result is True.


# Solution 4
# import unittest
# from unittest import mock
# from weather import WeatherAPI, WeatherAnalyzer


# class TestWeatherAnalyzer(unittest.TestCase):
#     def test_is_raining(self):
#         # Mocking weather data
#         weather_data = {
#             'weather': [
#                 {
#                     'main': 'Rain'
#                 }
#             ]
#         }
#         # Creating a mock weather API
#         weather_api = mock.MagicMock(spec=WeatherAPI)
#         weather_api.get_weather.return_value = weather_data
#         # Creating a WeatherAnalyzer instance
#         weather_analyzer = WeatherAnalyzer()
#         result = weather_analyzer.is_raining(weather_data)
#         # Asserting that the result is True
#         self.assertTrue(result)

# ==================================================================================
# Exercise 5
# Let's say you have a class called EmailClient that sends emails using a third-party email service, and a class called EmailSender that uses the EmailClient to send emails to a list of recipients. Here's the code for the EmailClient and EmailSender classes:


# import smtplib


# class EmailClient:
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password

#     def send_email(self, recipient, subject, body):
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(self.email, self.password)
#         message = f'Subject: {subject}\n\n{body}'
#         server.sendmail(self.email, recipient, message)
#         server.quit()

# class EmailSender:
#     def __init__(self, email_client):
#         self.email_client = email_client

#     def send_emails(self, recipients, subject, body):
#         for recipient in recipients:
#             self.email_client.send_email(recipient, subject, body)


# Define a class called TestEmailSender that inherits from unittest.TestCase. Write the unit tests using the unittest framework and the unittest.mock library to simulate sending emails. In the TestEmailSender class define one test case named test_send_emails().


# Create a mock EmailClient object using mock.MagicMock. Then create a list of recipients and an EmailSender instance using the mock EmailClient. Call the send_emails() method of the EmailSender with the list of recipients and some test email data. Assert that the send_email() method of the mock EmailClient was called twice with the correct arguments.


# Solution 5
# import unittest
# from unittest import mock
# from email_client import EmailClient, EmailSender


# class TestEmailSender(unittest.TestCase):
#     def test_send_emails(self):
#         # Mocking the EmailClient object
#         email_client = mock.MagicMock(spec=EmailClient)
#         # Creating a list of recipients
#         recipients = [
#             "recipient1@example.com",
#             "recipient2@example.com",
#         ]
#         # Creating an EmailSender instance
#         email_sender = EmailSender(email_client)
#         email_sender.send_emails(
#             recipients, "Test email", "This is a test email"
#         )
#         # Asserting that the was called twice with the correct arguments
#         email_client.send_email.assert_has_calls(
#             [
#                 mock.call(
#                     "recipient1@example.com",
#                     "Test email",
#                     "This is a test email",
#                 ),
#                 mock.call(
#                     "recipient2@example.com",
#                     "Test email",
#                     "This is a test email",
#                 ),
#             ]
#         )

# ==================================================================================
