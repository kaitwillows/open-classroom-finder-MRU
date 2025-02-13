import json
import code
from typing import List

global_i = 0 # ensures no enumerated dictionary keys are the same. there is no doubt a better way to do this

def dictionarize(item): # this recursively turns a json into a tree of dictionaries

    # TODO: docstrings maybe???

    if type(item) == type(""):
        try:
            json.loads(item) 
            # don't run the recursive call inside here, or else any Real errors won't show up.
            # thats not the best way to do it, but wtv, it works
            # TODO: more specific error handling
        except: 
            return item # BASE CASE - a string that cannot be jsonified
        return dictionarize(json.loads(item)) 

    elif type(item) == type([]):
        global global_i
        subdictionary = {}
        for subitem in item:
            subdictionary[f"{global_i}"] = dictionarize(subitem)
            global_i = global_i + 1
        return subdictionary
    
    elif type(item) == type({}): 
        for subkey in item:
            item[subkey] = dictionarize(item[subkey]) 
        return item
    elif type(item) == type(1):
        return f"{item}"
    elif type(item) == type(True):
        return item
    elif type(item) == type(None):
        return "null"







def write_data(input_jsons: List[str], output_json: str) -> None:
    # eat data
    data_list = []
    for input_file in input_jsons:
        f = open(input_file, "rt")
        data_list.append(f.read())
        f.close()
    tree = dictionarize(data_list)

    good_data = {}

    # digest data 
    for page in tree.keys():
        # print(tree[page]["data"].keys())
        for section_index in tree[page]["data"].keys():
            this_id = tree[page]["data"][section_index]["id"]
            this_entry = tree[page]["data"][section_index]
            good_data[this_id] = {}
            good_data[this_id]["courseTitle"] = this_entry["courseTitle"]
            good_data[this_id]["subjectDescription"] = this_entry["subjectDescription"]
            good_data[this_id]["subject"] = this_entry["subject"]
            good_data[this_id]["courseNumber"] = this_entry["courseNumber"]
            good_data[this_id]["sequenceNumber"] = this_entry["sequenceNumber"]
            good_data[this_id]["scheduleTypeDescription"] = this_entry["scheduleTypeDescription"]


            meetingTime = this_entry["meetingsFaculty"][list(this_entry["meetingsFaculty"].keys())[0]]["meetingTime"]

            good_data[this_id]["beginTime"] = meetingTime["beginTime"]
            good_data[this_id]["endTime"] = meetingTime["endTime"]
            good_data[this_id]["monday"] = meetingTime["monday"]
            good_data[this_id]["tuesday"] = meetingTime["tuesday"]
            good_data[this_id]["wednesday"] = meetingTime["wednesday"]
            good_data[this_id]["thursday"] = meetingTime["thursday"]
            good_data[this_id]["friday"] = meetingTime["friday"]
            good_data[this_id]["saturday"] = meetingTime["saturday"]
            good_data[this_id]["sunday"] = meetingTime["sunday"]
            good_data[this_id]["room"] = meetingTime["room"]
            # good_data[this_id][""] = meetingTime[""]

    # shit data
    output_json_data = json.dumps(good_data)
    f = open(output_json, "wt")
    f.write(output_json_data)
    f.close


    # code.interact(local = locals())

write_data(["./jsons/1.json","./jsons/2.json","./jsons/3.json","./jsons/4.json","./jsons/5.json"],  "meow.json")






# code.interact(local = locals())

# good_data[id] = 


# - id?:
# - termDesc
# - subjectCourse
# - sequenceNumber (i assume this is section)
# - scheduleTypeDescription
# - calc daysUsed (dictionary or hashmap)
# - startTime
# - endTime


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


# class Sections:
#     def __init__(self, ):
#         # TODO
#     def is_sheduled_today(day: str) -> bool:
#         # TODO
#     def minutes_free() -> int: # probably not a float?
#         # TODO

# code.interact(local = locals())
