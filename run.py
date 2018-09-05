import CreatePersons
import personDetect
import time

"""
input: a photo contains a group of faces

1. detect faces in the photo and get emotion data(depression level)
2. identify the faces and link them with depression level
3. update the depression level to the person under the data base
4. grab all the depression level on the data base and evaluate the data
5. if there is someone who cross the yellow line, the robot will give something to help the person
6. wait for some time

output: get the value associated with the person id, find whether he or she is sad
"""


"""
declare all the constant
"""
person_group = "techx"
image_path="/Users/multyxu/Desktop/1.jpg"
image_data=open(image_path, "rb").read()

"""
declare all the variables for processing
"""
#face_detect_info = personDetect.detect(image_data)
#face_id_detected = list(face_detect_info.keys()) #[id,id]
#face_value_detected = list(face_detect_info.values()) #[value,value]

#face_identify_info = personDetect.identify_person(face_id_detected, person_group)
#[{'faceId': "", 'candidates': [{'personId': '', 'confidence': float}]}]

def person_identified():
    i = 0
    identified_list=[]
    for i in range(len(face_id_detected)):
        identified_list.append(face_identify_info[i]['candidates'][0]['personId'])
    return identified_list

#print(face_value_detected)
#print(person_identified())
#print(face_identify_info[0]['candidates'][0]['personId'])


#get all person information
# return {'personId': userData}
def get_all_person_info():
    i = 0
    all_person_info={}
    for i in range(len(CreatePersons.list_person(person_group))):
        print(i)
        single_person_info={
            CreatePersons.list_person(person_group)[i]["personId"] : \
            CreatePersons.list_person(person_group)[i]["userData"] 
        }
        all_person_info.update(single_person_info)
    return all_person_info

#all_person_info=get_all_person_info()
# get all person id
# return [id, id, id]
#all_person_id = list(all_person_info.keys())


def update_detected_person():
    print("\nStart updating detected persons, we have "+ str(len(face_value_detected)) +"\n")
    # try :
    #     i = 0
    #     for i in range (len(face_value_detected)):
    #         print("\nUpdaing person:", i)
    #         CreatePersons.update_person(
    #             person_group,
    #             person_identified()[i],
    #             str(float( all_person_info[ person_identified()[i] ] ) \
    #             + float(face_value_detected[i]))
    #             )
    #     print("Done updating all detected persons")
    #     return "person updated"

    # except Exception as e:
    #     print(e)
    for person_current_face_id in face_id_detected:
        print("Updating person:", person_current_face_id)
        check_result = personDetect.identify_person([person_current_face_id], person_group)
        print(check_result)
        person_id_to_update = check_result[0]['candidates'][0]['personId']
        person_to_update_current_depression_level = face_detect_info[check_result[0]['faceId']]
        current_depression_level_on_cloud = all_person_info[person_id_to_update]
        new_depression = \
            float(current_depression_level_on_cloud) + \
            float(person_to_update_current_depression_level)
        print("The new derpession level is:", new_depression)
        CreatePersons.update_person(person_group, person_id_to_update, new_depression)

        

def evaluate_data():
    depress_person_id=[]
    i = 0
    for i in range(len(all_person_id)):
        user_data=float(all_person_info[all_person_id[i]])
        print(user_data)
        if user_data > 2.0:
            depress_person_id.append(all_person_id[i])
    return depress_person_id
    

print("Start Deteting ppl in the current picture.....")
face_detect_info = personDetect.detect(image_data)
face_id_detected = list(face_detect_info.keys())
face_value_detected = list(face_detect_info.values())
print("Done Deteting ppl in the current picture, start geting info for all could_faces")
# Get existing user list and corresponding data
all_person_info=get_all_person_info()
all_person_id = list(all_person_info.keys())
print("Done getting all could_faces, start checking if ppl in current pic exist in cloud_faces")
# Check if ppl exist in our cloud_faces
face_identify_info = personDetect.identify_person(face_id_detected, person_group)
print("Done checking ppl, starting update person in cloud_faces")    
update_result = update_detected_person()

    
depress_person=evaluate_data()
print(depress_person, "\n", all_person_info, face_detect_info)


    


