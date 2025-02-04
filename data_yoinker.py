def jsonize(item): # fuck your conventions, im calling it that
    try:
        item = json.loads(item) 
    except: # cant load bc its a string
        return item # yeah???
    # item itself is now a dictionary
    return jsonize(item) # item may become a dictionary

    
import json

json_file = open("classes.json", "rt")

data = json_file.read()

json_tree = jsonize(data)
print(json_tree["data"][0]) 


raw_class_list = json_tree["data"]

for item in raw_class:


# - id?:
# - termDesc
# - subjectCourse
# - sequenceNumber (i assume this is section)
# - scheduleTypeDescription
# - NO but then the meeting times are just in a one fucking item list what



# for each in class_list:
# well, hold on,
#   just copy all the entries we care about to dictionary, then append self to new_list
#   SEPERATE room_prefix and room_number
#   also note first number (floor)


#   json it
#   take important attributes, make key/value pairs in subdictionary
#   append k/v of id/subdictionary to class_dictionary

# that ^ gives a dictionary of dictionaries. 
# - for the subdict, thats good, but list might be best for outter pair????


# how should i save this data? when do i do that?
# save to dictionary, then to json

# json data:
# - key:id
# - room number
# - day of the week (later 
# - start time
# - end time
