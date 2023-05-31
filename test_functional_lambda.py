import unittest
import requests


class LambdaFunctionFunctionalTests(unittest.TestCase):
    def test_missing_path_should_return_404_response(self):
        ENDPOINT = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com"
        response = requests.get(ENDPOINT)
        self.assertEqual(response.status_code,404)
        self.assertEqual(response.text,'Please use a valid API /find/closecontacts,/find/locations,/find/people')

    def test_findpeople_should_return_successfully(self):
        ENDPOINT = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/people?location=Asshai&date=2021-02-01T00:00:00.000Z"
        response = requests.get(ENDPOINT)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.text,'["Bronn", "Jon Snow", "Sansa Stark"]')

    def test_findclosecontacts_should_return_successfully(self):
        ENDPOINT = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/closecontacts?person=Jon Snow&date=2021-02-01T00:00:00.000Z"
        response = requests.get(ENDPOINT)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.text,'["Bronn", "Sansa Stark", "Grey Worm", "Tywin Lannister", "Jaime Lannister"]')

    def test_findlocationsfor_should_return_successfully(self):
        ENDPOINT = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/locations?person=Bronn&date=2021-02-01T00:00:00.000Z"
        response = requests.get(ENDPOINT)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.text,'["Asshai", "Bear Island", "Myr", "The Eyrie"]')

    def test_missing_queries_findpeople_should_return_400_response(self):
        ENDPOINT_1 = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/people?location=Asshai"
        response_1 = requests.get(ENDPOINT_1)
        self.assertEqual(response_1.status_code,400)
        self.assertEqual(response_1.text,'Error using /find/people method. Date queryStringParameter is required.')

        ENDPOINT_2 = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/people?date=2021-02-01T00:00:00.000Z"
        response_2 = requests.get(ENDPOINT_2)
        self.assertEqual(response_2.status_code,400)
        self.assertEqual(response_2.text,'Error using /find/people method. Location queryStringParameter is required.')
        
        ENDPOINT_3 = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/people"
        response_3 = requests.get(ENDPOINT_3)
        self.assertEqual(response_3.status_code,400)
        self.assertEqual(response_3.text,'Error using /find/people method. Date queryStringParameter is required. Location queryStringParameter is required.')
    
    def test_missing_queries_findlocations_should_return_400_response(self):
        ENDPOINT_1 = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/locations?person=Bronn"
        response_1 = requests.get(ENDPOINT_1)
        self.assertEqual(response_1.status_code,400)
        self.assertEqual(response_1.text,'Error using /find/locations method. Date queryStringParameter is required.')

        ENDPOINT_2 = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/locations?date=2021-02-01T00:00:00.000Z"
        response_2 = requests.get(ENDPOINT_2)
        self.assertEqual(response_2.status_code,400)
        self.assertEqual(response_2.text,'Error using /find/locations method. Person queryStringParameter is required.')
        
        ENDPOINT_3 = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/locations"
        response_3 = requests.get(ENDPOINT_3)
        self.assertEqual(response_3.status_code,400)
        self.assertEqual(response_3.text,'Error using /find/locations method. Person queryStringParameter is required. Date queryStringParameter is required.')

    def test_missing_queries_findclosecontacts_should_return_400_response(self):
            ENDPOINT_1 = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/closecontacts?person=Bronn"
            response_1 = requests.get(ENDPOINT_1)
            self.assertEqual(response_1.status_code,400)
            self.assertEqual(response_1.text,'When using /find/closecontacts method. Date queryStringParameter is required.')

            ENDPOINT_2 = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/closecontacts?date=2021-02-01T00:00:00.000Z"
            response_2 = requests.get(ENDPOINT_2)
            self.assertEqual(response_2.status_code,400)
            self.assertEqual(response_2.text,'When using /find/closecontacts method. Person queryStringParameter is required.')
            
            ENDPOINT_3 = "https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/closecontacts"
            response_3 = requests.get(ENDPOINT_3)
            self.assertEqual(response_3.status_code,400)
            self.assertEqual(response_3.text,'When using /find/closecontacts method. Person queryStringParameter is required. Date queryStringParameter is required.')

if __name__ == '__main__':
    unittest.main()
