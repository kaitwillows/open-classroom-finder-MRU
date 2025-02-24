import json
import code

# find each unique room, and make it a key in the dictionary `rooms`
# each unique room will have
#   monday_bookings: [(start_time, end_time), (start_time, end_time)] # day and tuples cannot run in parallel
#       

# for efficiency, we should go building -> room -> tuples and floor

def main():
    thing_doer("sections.json", "test.json")



def thing_doer(input_file: str, output_file: str) -> None: # its late and im tired
    # wings[wing][room][day][bookedTimes] = [...]
    wings = {}
    f = open(input_file, "rt")
    sections = json.loads(f.read())
    f.close()


    for section_key in sections.keys():
        wing = sections[section_key]["room"].rstrip("1234567890") # presumably, this works
        room = sections[section_key]["room"]
        daysBooked = sections[section_key]["daysBooked"]
        timeBooked = sections[section_key]["timeBooked"] # i see why shit like this should be abstracted oh (fuck)

        for day in daysBooked:
            try:
                wings[wing][room][day].append(timeBooked)
            except KeyError: 
                try:
                    wings[wing][room][day] = []
                    wings[wing][room][day].append(timeBooked)
                except KeyError:
                    try:
                        wings[wing][room] = {}
                        wings[wing][room][day] = []
                        wings[wing][room][day].append(timeBooked)
                    except KeyError:
                        wings[wing] = {}
                        wings[wing][room] = {}
                        wings[wing][room][day] = []
                        wings[wing][room][day].append(timeBooked)
    f = open(output_file, "wt")
    f.write(json.dumps(wings))
    f.close()




    code.interact(local = locals())
main()    
    


# # pretend the following is a single section listing
# room_number = "b200"
# days_booked = ["monday", "wednesday"]
# time_booked = (1200, 1320)
# 
# 
# for day in days_booked:
# 
#     # the goal is to write the nested data, but if there isnt a place for it to go, then you must make one, but without overwriting existing data
#     # and so, this try/catch mess is needed
#     try:
#         rooms[room_number][day].append(time_booked)
#     except KeyError: # either `room_number` doesn't exist yet, or `day` doesn't exist yet
#         try:
#             rooms[room_number][day] = [] # make `day` list exist
#             rooms[room_number][day].append(time_booked)
#         except KeyError: # so then, it's `room_number` that doesn't exist
#             rooms[room_number] = {} 
#             rooms[room_number][day] = []
#             rooms[room_number][day].append(time_booked)



