import CreatePersons
import personDetect


person_group = "techx"
image_path="/Users/multyxu/Desktop/7.jpg"
image_data=open(image_path, "rb").read()


#CreatePersons.createGroup("techx", "Techx training", "")
#CreatePersons.create_new_person("techx", "Stacey", "")

"""
image_name=201804131158
for i in range(100):
    image_path="/Users/multyxu/Desktop/Polished/Stacey/%sDesZ.JPG"%image_name
    CreatePersons.add_face(image_path,"techx",'78be74a6-90b0-487f-8c28-bd7c25ef8e43')
    image_name+=1

"""

"""
CreatePersons.update_person("techx", 'b3cd8903-4d43-4191-ab87-740fbff6cb41', "1.9")
CreatePersons.update_person("techx", 'e8305464-7a97-4d39-996e-140a785cb571', "1.9")
CreatePersons.update_person("techx", '78be74a6-90b0-487f-8c28-bd7c25ef8e43', "1.9")
print(CreatePersons.list_person("techx"))
"""

'''
CreatePersons.update_person("techx", 'e8305464-7a97-4d39-996e-140a785cb571', "0.0")
print(CreatePersons.list_person("techx"))
'''

print(personDetect.detect(image_data))
