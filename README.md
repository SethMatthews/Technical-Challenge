# Technical-Challenge

## Problem Statement
Consider the principle of *Contact Tracing*: Individuals check in on various dates at various locations to facilitate rapid notification in the event of an outbreak. Naturally contact tracing information is collated in two ways:
1. A location provides a list of persons and what date they attended
2. A person provides a list of locations and what date they attended

The attached file [`data.json`](./data.json) contains contact tracing data of the first kind. Your mission is to: 

```
DESIGN and DEPLOY a web API that allows users to:
- Find every PERSON that has visited a particular LOCATION on a particular date
- Find every LOCATION that a particular PERSON has visited on a particular date
- [BONUS] given a specific PERSON and date, identify their CLOSE CONTACTS on that date

Write DOCUMENTATION explaining how to use your API, and the reasoning behind your architectual decisions in a `README`

Package your SOURCE CODE into a single `git` repo for submission
```

You may make the following assumptions:
- Names of people and locations are globally unique
- Attendance on the same date constitutes close contact
- Data is sorted alphanumerically


# API Documentation

The public URL endpoint of the API is https://gl4go60ush.execute-api.us-east-1.amazonaws.com



| API |  Description  |
|:-----|------:|
| `/find/people`   | `GET` Find every PERSON that has visited a particular LOCATION on a particular date  |
| `/find/locations`   | `GET` Find every LOCATION that a particular PERSON has visited on a particular date  |
| `/find/closecontacts`   | `GET` Given a specific PERSON and date, identify their CLOSE CONTACTS on that date | 


## /find/people
| URL Parameter |  Details  |
|:-----|------:|
| `location`   | `string` The location to search for  |
| `date`   |  `datetime` The date to search for. Must be a valid ISO Strings at midnight UTC  |

Example:
https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/people?location=Asshai&date=2021-02-01T00:00:00.000Z

Example Output:

` ["Bronn", "Jon Snow", "Sansa Stark"] `



## /find/locations
| URL Parameter |  Details  |
|:-----|------:|
| `person`   | `string` The person to search for   |
| `date`   |  `datetime` The date to search for. Must be a valid ISO Strings at midnight UTC   |

Example:
https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/locations?person=Bronn&date=2021-02-01T00:00:00.000Z

Example Output:

` ["Asshai", "Bear Island", "Myr", "The Eyrie"] `


## /find/closecontacts
| URL Parameter |  Details  |
|:-----|------:|
| `person`   | `string` The contact to search for  |
| `date`   |  `datetime` The date to search for. Must be a valid ISO Strings at midnight UTC   |

Example:
https://gl4go60ush.execute-api.us-east-1.amazonaws.com/find/closecontacts?person=Bronn&date=2021-02-01T00:00:00.000Z

Example Output:

` ["Jon Snow", "Sansa Stark", "Catelyn Stark", "Robb Stark", "Samwell Tarly", "Theon Greyjoy", "Daenerys Targaryen", "Joffrey Baratheon", "Margaery Tyrell"] `

## Important Notes 
-  The date should be referenced using the ISO Strings at midnight UTC, for example the 28th of February 2021 needs to be referenced as 2021-02-28T00:00:00.000Z 
- URL parameters such as person, location and date need to exactly match the string in the file [`data.json`](./data.json). Hence, queries are case sensitive.
- People with middle names are intentionally returned in the same format as they occur in the file [`data.json`](./data.json), for example `Eddard \"Ned\" Stark` 


# Rationale behind my architectual decisions


## AWS Infrastructure Rationale

![diagram-infra-aws](https://user-images.githubusercontent.com/50725246/230691031-c37e1ad4-4f1e-4280-9d1f-5ec3c270a0f1.svg)


The entire infrastructure for this project can be seen in the cloudformation document [`IAC.yaml`](./IAC.yaml) and [`CICD_IAC.yaml`](./CICD_IAC.yaml). These two files could have been combined if I had more time.


Given the problem, "DESIGN and DEPLOY a web API" combined with my knowledge of AWS, it seemed sensible to utilise the AWS API Gateway service. This allows the creation of robust, secure, and scalable APIs that can access Amazon Web Services or other web services. 

A RESTful API product was used instead of a WebSockets API because RESTful API's are tailored for retrieving, creating, and managing resources.
 
A HTTP API was choosen over a REST API because the HTTP API met all the required features for the problem, cost a lot less and performs slightly better. If in production you want any of the following features such as API keys, per-client throttling, request validation, AWS WAF integration, or private API endpoints, a REST API may be better.


I chose to use a lambda function as my backend, as the HTTP API integrates nicely with Lambda functions. Also, you get all the added benefits of using a function as a service (FaaS) including greater scalability, more flexibility, reduced cost, and no need to worry about purchasing, provisioning, and managing backend servers. 

The following four (GET methods) routes were added:
- /find/people
- /find/locations
- /find/closecontacts
- /

All four routes integrated to the same backend lambda function when they received a request.

These four routes could have been integrated with a separate lambda function each, however all routes were integrated with the same lambda function to simplify and avoid repeating code.

This was acheived by using the event['rawPath'] and event["queryStringParameters"], which was already passed to the lambda function, to determine which search method and parameters to use respectively.

Please also note, the fourth route being a GET method of the route "/ " was created with the intention to be a catch all route for the API. However, $default appears to be the catch all route for AWS API Gateway although there seems to be some confliction with my API Gateway Stage (my API also uses $default for the Stage). If I had more time on this project, I would try implement a catch all route correctly and return 404 response errors for requests that do not use a valid path such as /find/closecontacts,/find/locations,/find/people.



## CI/CD AWS CodePipeline Rationale

Diagram of code pipeline
![Pipeline-Diagram](https://user-images.githubusercontent.com/50725246/230542845-c6c6c750-63de-4202-a52e-219644a0b6bf.svg)


A CI/CD Pipeline was created using AWS CodePipeline. So any push action in this repository will cause the CodePipeline to trigger a build in AWS CodeBuild, where the contents of the GitHub repository is cloned into a linux Docker environment. From there, the buildspec.yml is executed, and the [`lambda_function.py`](./lambda_function.py) and [`data.json`](./data.json) files are zipped into one file and sent to the root of the lambda code directory. After this completes the API should be fully funtional. 

This whole CI/CD pipeline has be defined as infrastructure as code in the [`CICD_IAC.yaml`](./CICD_IAC.yaml) file. Whilst the Lambda and API Gateway has been defined as infrastructure as code in the [`IAC.yaml`](./IAC.yaml) file.  

When writing my infrastructure as code I tried to use account id and region references when naming resources, to ensure ARN's and S3 bucket names were globally unique and to allow for the stack to be more account and region portable.

## Important Notes about Infrastructure 
- The [`IAC.yaml`](./IAC.yaml) stack should be built first, before the  [`CICD_IAC.yaml`](./CICD_IAC.yaml) stack.
- The [`CICD_IAC.yaml`](./CICD_IAC.yaml) file wont launch in any other AWS account apart from mine because of the current codestar resource connection is linked to my acount (if I had more time I would make code connection with a token in AWS secrets manager, so someone could just make a new connection and store their token in AWS Secret Manager and launch the stack). 
- If you want to delete the  [`CICD_IAC.yaml`](./CICD_IAC.yaml) stack, you  will have to empty the codepipeline s3 bucket before deleting the stack  (I'm sure there is some work around with a custom cfn resource and lambda function and would try and resolve this given more time).
- If I had more time I would have integrated pytest into the pipeline with reporting. Ideally the CI/CD pipeline would conduct all my testing on a development API and lambda, before deploying to the production API and lambda.

## Python Script Rationale 
- The [`data.json`](./data.json) file is stored with the [`lambda_function.py`](./lambda_function.py) in the root directory of the lambda function because storing the data file in the same directory allows the lambda function to quickly search the data, as it is in the same local lambda environment.
- The python script uses a simple brute force search to find the relevant information. However a more efficient search type, such as a binary search could have been used instead as the data is sorted alphanumerically. Although a binary search would have been faster than a brute force search, it would have made the pythonscript more complex. However, due to the data set being small in size, the brute force search execution time was insignicant and hence the added complexity of using a binary search did not seem worth it.
- I decided that dates could be queried from the API using an ISO Strings at midnight UTC format (i.e. 2021-02-28T00:00:00.000Z), because it made it simple to program due to this being the same format of the dates in the [`data.json`](./data.json) file.
- Unit, Integration and Functional testing can be run manually using the following commands, respectively.
```
python3 test_unit_lambda.py 
python3 test_integration_lambda.py
python3 test_functional_lambda.py
```


# How I Would Improve My Design  

I would have integrated pytest into my CodePipeline, with some CodeBuild reporting funtionality. A picture of this reporting feature can be seen below.

<img width="1508" alt="PyTest_Reporting_Image" src="https://user-images.githubusercontent.com/50725246/230749919-c6fc5a07-52da-4f05-a388-b185836c4371.png">

Also, my ideal infrastructure can be seen in the diagram below.


![Ideal-Pipeline-Diagram drawio](https://user-images.githubusercontent.com/50725246/230749318-d9ed9b1d-3e67-4aca-a7e5-a97e8b2a81cf.svg)

This infrastructure would ensure every git commit passes all unit and integration testing before deploying to a development environment.

 From there, all git commits will undergo functional (end-to-end) tests on the development environment, to ensure the development API endpoints are working as expected. 
 
 Then after passing all functional tests, it will move on to the next stage, building and deploying a production environment.
  
  After the production environment is built, a final functional (end-to-end) test will be conducted to ensure the production environment API endpoints are working as expected. If this test fails, the development team will be alerted.



Furthermore, I would restructure my file system for this git repo to something more maintainable. For example: 
- .gitigonore
- README.md
- buildspec.yml
- app 
    - lambda_funtion.py 
    - data.json
    - tests
        - test_unit_lambda.py
        - test_integration_lambda.py 
        - test_functional_lambda.py 
- infrastructure 
    - IAC.yaml
