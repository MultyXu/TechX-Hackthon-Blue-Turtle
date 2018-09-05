import requests
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# declare all the variable that used in the following function
url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/"
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '71bc9a58462e4196888cc4856cfa5a11',
}
#variables for createGroup
#personGroupId = "3"
name = '3'
#body = "{ 'name':'group1', 'userData':'//put data here' }"



"""
functions for process person groups
"""

# function for create a person group, cannot create a group with same id
#return an empty set
def createGroup(personGroupId, groupName, userData):
    try:
        create_new_group_url = url+"persongroups/%s"%(personGroupId)
        json = {
            'name':groupName,
            'userData':userData,
            }
        response = requests.put(create_new_group_url, json=json,headers=headers)
        new_group_info = response.json()
        print(new_group_info)
        
#        body = "{ 'name': '%s', 'userData': '%s'}"%(groupName, userData)
#        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
#        conn.request("PUT", "/face/v1.0/persongroups/%s"%personGroupId, body, headers)
#        response = conn.getresponse()
#
#        print(response.reason)
#
#        conn.close()
    except Exception as e:
        print(e.args)


#training a person group
#return empty ####
def train_person_group(personGroupId, userData):
    train_person_group_url = url+"persongroups/%s/train"%personGroupId
    response=requests.post(train_person_group_url, data=userData, headers=headers)
    print(response.text,"person group trained")
 #   train=response.json()


#get train status
#return training status
def get_group_status(personGroupId):
    try:
        get_group_status_url=url+"persongroups/%s/training"%personGroupId
        response=requests.get(get_group_status, headers=headers)
        get_group_status_info=response.json()
        print(get_group_status_info)
        
    except Exception as e:
        print(e.args)


"""
functions for process persons
"""

#functions for create a new person
#return a person id
def create_new_person(personGroupId, personName, userData):
    try:
        create_new_person_url = url+"persongroups/%s/persons"%personGroupId
        json = {
            'name':personName,
            'userData':userData,
            }
        response = requests.post(create_new_person_url, json=json, headers=headers)
        new_person_info = response.json()
        print(new_person_info)
        
    except Exception as e:
        print(e.args)


#for get the information of a person through group id and person id
#return person information
def get_person_info(personGroupId, personId):
    try:
        get_person_info_url = url+"persongroups/%s/persons/%s"%(personGroupId, personId)
        response=requests.get(get_person_info_url, headers=headers)
        person_info=response.json()
        print("person_info get\n")
        return person_info
    
    except Exception as e:
        print(e.args)


#list all the people in a specific perosn group
#an array of person information
def list_person(personGroupId, start=None, top=None):
    list_person_url=url+"persongroups/%s/persons"%personGroupId
    params={
        'start':start,
        'top':top,
        }
    response=requests.get(list_person_url, params=params, headers=headers)
    list_person_info=response.json()
    return list_person_info


#add a face under a person
#return a persisted face id
def add_face(image_path, personGroupId, personId, userData=None, target_face=None):
    add_face_url=url+"persongroups/%s/persons/%s/persistedFaces"%(personGroupId, personId)
    image_data=open(image_path, "rb").read()
    json=None
    image_headers={
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '71bc9a58462e4196888cc4856cfa5a11',
        }
    params={
        'userData':userData,
        'targetFace':target_face,
        }
    response=requests.post(add_face_url, params=params, headers=image_headers, data=image_data)
    persisted_face_id=response.json()
    print("persisted_face_id get\n")
    return persisted_face_id


#update user data
#return empty
def update_person(personGroupId, personId,depress_level):
    update_person_url=url+"persongroups/%s/persons/%s"%(personGroupId, personId)
    json={
        'userData':depress_level,
        }
    response=requests.patch(update_person_url, json=json, headers=headers)
    print("person updated")
    return None

        
"""
using functions
"""
#createGroup(personGroupId, name,"")
#create_new_person(personGroupId, "Multy","")
#get_person_info("3", '24892dc1-7026-4d2a-ac77-3ad40f19ac36')
#list_person("3")
#add_face(
#    "/Users/multyxu/Desktop/unknown_face.jpg",
#    "3",
#    '24892dc1-7026-4d2a-ac77-3ad40f19ac36',
#    )
#train_person_group("3", "")


