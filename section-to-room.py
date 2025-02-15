import json
import code

# find each unique room, and make it a key in the dictionary `rooms`
# each unique room will have
#   monday_bookings: [(start_time, end_time), (start_time, end_time)] # day and tuples cannot run in parallel
#       



thing_doer(input_file: str, output_file: str) -> None: # its late and im tired
    rooms = {}
    



















code.interact(local = locals())


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
