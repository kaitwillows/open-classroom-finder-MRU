def dictionarize(item): # fuck your conventions, im calling it that
    
    try:
        return json.loads(item) 
    except: # cant load bc its not a string or list (hopefully)
        pass
    if type(item) == type(""): # im so sorry to anyone reading this
        return item
    elif type(item) == type([]):
        subdictionary = {}
        for i, subitem in enumerate(item):
            subdictionary[f"{i}"] = dictionarize(item)
        return subdictionary
    print("HELLO SOMETHING WENT WERID")

    # elif type(item) == type({}):
    #     dictionarize(json.loads(item)) 

    
import json
import code

f = open("classes.json", "rt")
data = f.read()
f.close()

tree = dictionarize(data)


class Sections:
    def __init__(self, ):
        # TODO
    def is_sheduled_today(day: str) -> bool:
        # TODO
    def minutes_free() -> int: # probably not a float?
        # TODO



# - id?:
# - termDesc
# - subjectCourse
# - sequenceNumber (i assume this is section)
# - scheduleTypeDescription
# - daysUsed (dictionary or hashmap)
# - times


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

code.interact(local = locals())
