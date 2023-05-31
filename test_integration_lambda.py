import unittest
import lambda_function

import json


class LambdaFunctionIntegrationTests(unittest.TestCase):
    def test_findclosecontacts_should_return_successfully(self):
        sample_event = {'version': '2.0', 'routeKey': 'GET /find/closecontacts', 'rawPath': '/find/closecontacts', 'rawQueryString': 'person=Jon%20Snow&date=2021-02-01T00:00:00.000Z', 'headers': {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'content-length': '0', 'host': 'l57zn1qk42.execute-api.us-east-1.amazonaws.com', 'postman-token': '548a93fb-2ae6-49b5-acb2-577cace9907c', 'user-agent': 'PostmanRuntime/7.29.2', 'x-amzn-trace-id': 'Root=1-642cbce8-109359796c4d0ce41e1a440f', 'x-forwarded-for': '122.199.44.88', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https'}, 'queryStringParameters': {'date': '2021-02-01T00:00:00.000Z', 'person': 'Jon Snow'}, 'requestContext': {'accountId': '844067823212', 'apiId': 'l57zn1qk42', 'domainName': 'l57zn1qk42.execute-api.us-east-1.amazonaws.com', 'domainPrefix': 'l57zn1qk42', 'http': {'method': 'GET', 'path': '/find/closecontacts', 'protocol': 'HTTP/1.1', 'sourceIp': '122.199.44.88', 'userAgent': 'PostmanRuntime/7.29.2'}, 'requestId': 'C4J0ZhuBoAMEV4g=', 'routeKey': 'GET /find/closecontacts', 'stage': '$default', 'time': '05/Apr/2023:00:12:24 +0000', 'timeEpoch': 1680653544633}, 'isBase64Encoded': False}
        result = lambda_function.lambda_handler(sample_event,0)
        self.assertEqual(result,{'statusCode': 200, 'body': json.dumps(["Bronn", "Sansa Stark", "Grey Worm", "Tywin Lannister", "Jaime Lannister"])})
    
    def test_findpeople_should_return_successfully(self):
        sample_event = {'version': '2.0', 'routeKey': 'GET /find/people', 'rawPath': '/find/people', 'rawQueryString': 'location=Asshai&date=2021-02-01T00:00:00.000Z', 'headers': {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'content-length': '0', 'host': 'l57zn1qk42.execute-api.us-east-1.amazonaws.com', 'postman-token': '3285d747-5281-4b38-a1fb-98a66aaa3f4f', 'user-agent': 'PostmanRuntime/7.29.2', 'x-amzn-trace-id': 'Root=1-642cbb94-7070d4d5036937884e696fdb', 'x-forwarded-for': '122.199.44.88', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https'}, 'queryStringParameters': {'date': '2021-02-01T00:00:00.000Z', 'location': 'Asshai'}, 'requestContext': {'accountId': '844067823212', 'apiId': 'l57zn1qk42', 'domainName': 'l57zn1qk42.execute-api.us-east-1.amazonaws.com', 'domainPrefix': 'l57zn1qk42', 'http': {'method': 'GET', 'path': '/find/people', 'protocol': 'HTTP/1.1', 'sourceIp': '122.199.44.88', 'userAgent': 'PostmanRuntime/7.29.2'}, 'requestId': 'C4I_TjMGoAMEVrQ=', 'routeKey': 'GET /find/people', 'stage': '$default', 'time': '05/Apr/2023:00:06:44 +0000', 'timeEpoch': 1680653204877}, 'isBase64Encoded': False}
        result = lambda_function.lambda_handler(sample_event,0)
        self.assertEqual(result,{'statusCode': 200, 'body': json.dumps(["Bronn", "Jon Snow", "Sansa Stark"])})
    
    def test_findlocationsfor_should_return_successfully(self):
        sample_event ={'version': '2.0', 'routeKey': 'GET /find/locations', 'rawPath': '/find/locations', 'rawQueryString': 'person=Jon%20Snow&date=2021-02-01T00:00:00.000Z', 'headers': {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'content-length': '0', 'host': 'l57zn1qk42.execute-api.us-east-1.amazonaws.com', 'postman-token': '5e379b5a-c818-4341-9d77-8a8769bc990a', 'user-agent': 'PostmanRuntime/7.29.2', 'x-amzn-trace-id': 'Root=1-642cbce6-72d5267d1522835479c89747', 'x-forwarded-for': '122.199.44.88', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https'}, 'queryStringParameters': {'date': '2021-02-01T00:00:00.000Z', 'person': 'Jon Snow'}, 'requestContext': {'accountId': '844067823212', 'apiId': 'l57zn1qk42', 'domainName': 'l57zn1qk42.execute-api.us-east-1.amazonaws.com', 'domainPrefix': 'l57zn1qk42', 'http': {'method': 'GET', 'path': '/find/locations', 'protocol': 'HTTP/1.1', 'sourceIp': '122.199.44.88', 'userAgent': 'PostmanRuntime/7.29.2'}, 'requestId': 'C4J0CjjFIAMEVzw=', 'routeKey': 'GET /find/locations', 'stage': '$default', 'time': '05/Apr/2023:00:12:22 +0000', 'timeEpoch': 1680653542368}, 'isBase64Encoded': False}
        result = lambda_function.lambda_handler(sample_event,0)
        self.assertEqual(result,{'statusCode': 200, 'body': json.dumps(["Asshai", "Braavos", "Fist of the First Men", "Moat Cailin"])})

    def test_missing_path_should_return_404_response(self):
        sample_event = {'version': '2.0', 'routeKey': 'GET /', 'rawPath': '/', 'rawQueryString': '', 'headers': {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.5', 'content-length': '0', 'dnt': '1', 'host': 'gl4go60ush.execute-api.us-east-1.amazonaws.com', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'cross-site', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0', 'x-amzn-trace-id': 'Root=1-6430afe5-4ba555587881e2197e835c15', 'x-forwarded-for': '122.199.44.88', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https'}, 'requestContext': {'accountId': '844067823212', 'apiId': 'gl4go60ush', 'domainName': 'gl4go60ush.execute-api.us-east-1.amazonaws.com', 'domainPrefix': 'gl4go60ush', 'http': {'method': 'GET', 'path': '/', 'protocol': 'HTTP/1.1', 'sourceIp': '122.199.44.88', 'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0'}, 'requestId': 'DCBr5iZ7oAMEVWg=', 'routeKey': 'GET /', 'stage': '$default', 'time': '08/Apr/2023:00:05:57 +0000', 'timeEpoch': 1680912357409}, 'isBase64Encoded': False}
        result = lambda_function.lambda_handler(sample_event,0)
        self.assertEqual(result,{'statusCode': 404, 'body': 'Please use a valid API /find/closecontacts,/find/locations,/find/people'})


if __name__ == '__main__':
    unittest.main()
