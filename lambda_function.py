import json

def loadJson(json_filename):
    file = open(json_filename)
    data = json.load(file)
    return data

contact_tracing_data = loadJson('data.json') 




def isDateIn(particular_date,list_of_dates): 
    """Returns true if the specified date is in the list of dates, else returns false """
    for date in list_of_dates:
        if date == particular_date:
            return True
    return False


def getLocation(particular_location): 
    """Returns the location object of the a particular LOCATION specified"""
    for location in contact_tracing_data:
        if location["location"] == particular_location:
            return location

def findPeople(particular_location, date): 
    """Returns an array of every PERSON that has visited a particular LOCATION on a particular date"""
    matching_people_list = []
    location = getLocation(particular_location)
    for person in location["persons"]:
        if isDateIn(date,person["dates"]):
            matching_people_list.append(person["person"])
    return matching_people_list 
    

def findLocationsFor(particular_person,particular_date):
    """Returns list of every LOCATION that a particular PERSON has visited on a particular date"""
    matching_locations_list = []
    for location in contact_tracing_data:
        for person in location["persons"]:
            if person["person"]==particular_person :
                if isDateIn(particular_date,person["dates"]):
                    matching_locations_list.append(location["location"])
    return matching_locations_list


def findCloseContacts(particular_person,particular_date): 
    """Returns list of CLOSE CONTACTS of a particular PERSON and on a particular date"""
    close_contacts= []
    hotspots = findLocationsFor(particular_person,particular_date)
    
    for hotspot in hotspots:
        for contact in findPeople(hotspot, particular_date):
            if contact not in close_contacts and contact!=particular_person: 
                close_contacts.append(contact)
    return close_contacts 




def lambda_handler(event, context):
    if event['rawPath']== '/find/people':
        query_error = "Error using /find/people method."
        try:
            date_query = event["queryStringParameters"]["date"]
        except:
            query_error += " Date queryStringParameter is required."
        try:
            location_query = event["queryStringParameters"]["location"]
        except:
            query_error += " Location queryStringParameter is required."
        
        if query_error != "Error using /find/people method.":
            return {
                'statusCode': 400,
                'body': query_error
            }
        body = findPeople(location_query,date_query)
        return {
            'statusCode': 200,
            'body': json.dumps(body)
        }


    
    elif event['rawPath']== '/find/locations':

        query_error = "Error using /find/locations method."
        try:
            person_query = event["queryStringParameters"]["person"]
        except:
            query_error += " Person queryStringParameter is required."
        try:
            date_query = event["queryStringParameters"]["date"]
        except:
            query_error += " Date queryStringParameter is required."
    
        if query_error != "Error using /find/locations method.":
            return {
                'statusCode': 400,
                'body': query_error
            }
        body = findLocationsFor(person_query,date_query)
        return {
            'statusCode': 200,
            'body': json.dumps(body)
        }
        
    elif event['rawPath']== '/find/closecontacts':

        query_error = "When using /find/closecontacts method."
        try:
            person_query = event["queryStringParameters"]["person"]
        except:
            query_error += " Person queryStringParameter is required."
        try:
            date_query = event["queryStringParameters"]["date"]
        except:
            query_error += " Date queryStringParameter is required."
    
        if query_error != "When using /find/closecontacts method.":
            return {
                'statusCode': 400,
                'body': query_error
            }

        body = findCloseContacts(person_query,date_query)
        return {
            'statusCode': 200,
            'body': json.dumps(body)
        }
    
    # only root endpoint 
    return {
        'statusCode': 404,
        'body': "Please use a valid API /find/closecontacts,/find/locations,/find/people"
    }

