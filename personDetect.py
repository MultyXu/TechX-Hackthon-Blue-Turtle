import requests
import CreatePersons
#face_api_url = "https://eastasia.api.cognitive.microsoft.com/face/v1.0/"

url ="https://westcentralus.api.cognitive.microsoft.com/face/v1.0/"


key_1 = "8e15b41d11864d50953bd1737427d39e"
key_2 = "a316d54c67dd4e17999af7154823a9d5"

image_name = "1.jpg"
image_path = "/Users/multyxu/Desktop/"+image_name
image_data = open(image_path, "rb").read()

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '71bc9a58462e4196888cc4856cfa5a11',
}


#detect a face from local photo
#return face id and emotion
def detect(image_data):
    params = {
        'returnFaceId': 'true',        
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes':  'emotion',
        }

    response = requests.post(url+"detect", params=params, headers=headers, data=image_data)
    face_info = response.json()

#    return face_info
    print(face_info)
    transmit_dc = {}
#   for i in range(len(face_info)):
#        append_dict = {face_info[i]["faceId"]: max(face_info[i]["faceAttributes"]["emotion"], key=face_info[i]["faceAttributes"]["emotion"].get )}
#        data_set.update(append_dict)
#        i += 1
    for i in range(len(face_info)):

        #print(face_info[i]["faceId"], face_info[i]["faceAttributes"]["emotion"])
        happiness_constant = (
            face_info[i]["faceAttributes"]["emotion"]["happiness"] +
            face_info[i]["faceAttributes"]["emotion"]["surprise"]
            )

        sadness_constant = (
            face_info[i]["faceAttributes"]["emotion"]["sadness"] +
            face_info[i]["faceAttributes"]["emotion"]["disgust"] +
            face_info[i]["faceAttributes"]["emotion"]["contempt"] +
            face_info[i]["faceAttributes"]["emotion"]["anger"] +
            face_info[i]["faceAttributes"]["emotion"]["fear"] +
            face_info[i]["faceAttributes"]["emotion"]["neutral"]/8102
            )

        depression_constant = sadness_constant - happiness_constant

        transmit_append={face_info[i]["faceId"]: depression_constant}
        transmit_dc.update(transmit_append)
        
    return transmit_dc

def identify_person(
    face_ids,
    person_group_id,
    large_person_group_id=None,
    max_candidates_return=1,
    threshold=None,
    ):
    identify_person_url=url+"identify"
    
    identify_headers={
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '71bc9a58462e4196888cc4856cfa5a11',
        }
    
    json={
        'personGroupId': person_group_id,
        'largePersonGroupId': large_person_group_id,
        'faceIds': face_ids,
        'maxNumOfCandidatesReturned': max_candidates_return,
        'confidenceThreshold': threshold,
        }
    
    response=requests.post(identify_person_url, json=json, headers=identify_headers)
    identiry_person_info=response.json()
    return identiry_person_info


#print(type(detect(image_data)))
#CreatePersons.get_person_info("3", '24892dc1-7026-4d2a-ac77-3ad40f19ac36')
#CreatePersons.add_face("/Users/multyxu/Desktop/1.jpg", "3", '24892dc1-7026-4d2a-ac77-3ad40f19ac36',"")
#CreatePersons.train_person_group("3")
#print(identify_person(list(detect(image_data).keys()),"3"))
