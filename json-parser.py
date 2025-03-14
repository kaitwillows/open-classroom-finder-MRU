import json
import code
from typing import List

global_i = 0 # ensures no enumerated dictionary keys are the same. there is no doubt a better way to do this

def dictionarize(item): # this recursively turns a json into a tree of dictionaries
    '''recursively organizes json data into dictionary tree for easier handling
    
    notes:
        - the `global_i` thing might be an exceptionally shitty workaround
    '''

    if type(item) == type(""):
        try:
            return int(item) # please just work
        except:
            pass
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
        return item
    elif type(item) == type(True):
        return item
    elif type(item) == type(None):
        return "null"



def write_data(input_jsons: List[str], output_json: str) -> None:
    '''writes a json file with relevant information in terms of class sections
    '''
    
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


            meetingTime = this_entry["meetingsFaculty"][list(this_entry["meetingsFaculty"].keys())[0]]["meetingTime"] # TODO: make this readable

            good_data[this_id]["timeBooked"] = (meetingTime["beginTime"],meetingTime["endTime"])

            good_data[this_id]["daysBooked"] = []

            if meetingTime["monday"] == True:
                good_data[this_id]["daysBooked"].append("monday")
            if meetingTime["tuesday"] == True:
                good_data[this_id]["daysBooked"].append("tuesday")
            if meetingTime["wednesday"] == True:
                good_data[this_id]["daysBooked"].append("wednesday")
            if meetingTime["thursday"] == True:
                good_data[this_id]["daysBooked"].append("thursday")
            if meetingTime["friday"] == True:
                good_data[this_id]["daysBooked"].append("friday")
            if meetingTime["saturday"] == True:
                good_data[this_id]["daysBooked"].append("saturday")
            if meetingTime["sunday"] == True:
                good_data[this_id]["daysBooked"].append("sunday")
            good_data[this_id]["room"] = meetingTime["room"]

    # shit data
    output_json_data = json.dumps(good_data)
    f = open(output_json, "wt")
    f.write(output_json_data)
    f.close


write_data(["./jsons/1.json","./jsons/2.json","./jsons/3.json","./jsons/4.json","./jsons/5.json"],  "sections.json")
