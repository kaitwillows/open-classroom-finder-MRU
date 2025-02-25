import code
import json
import room_time
# import type


def main():

    #find_the_openest("rooms.json", "monday", 1701)
    find_the_longestest("rooms.json", "tuesday", 951, "B")


def find_the_longestest(input_file, day, time, wing):
    f = open(input_file, "rt")
    wings = json.loads(f.read())
    f.close()

    print(f"day: {day}\ntime: {time}\nwing: {wing}\n")

    open_rooms = [] # open_rooms[n] = ("EA1200", 300) (minutes till booked)
    for room in wings[wing].keys():
        # first, is it actually open?
        if time_till_booked(day, time, wing, wings[wing][room]) >= 0:
            open_rooms.append((room, time_till_booked(day, time, wing, wings[wing][room])))
    for room in open_rooms:
        print(f"{room[0]} is booked in {room[1]} minutes")



def time_till_booked(day, time, wing, room):
    current_shortest_time = 0
    try:
        for time_slot in room[day]:
            if (convert_time(time) > convert_time(time_slot[0]) and (convert_time(time) < convert_time(time_slot[1]))):
                #ruh roh, we're booked
                return -1
            if (convert_time(time_slot[0]) - convert_time(time)) < current_shortest_time:
                current_shortest_time = convert_time(time_slot[0]) - convert_time(time)
        return current_shortest_time
    except KeyError:
        return -1

    



def find_the_openest(input_file, day, time): # basically, whats gonna be open till tomorrwo
    f = open(input_file, "rt")
    wings = json.loads(f.read())
    f.close()

    # basically, we want nothing that *ends* after the specified time, or any room where Not(time[1] > time)
    print(f"day: {day}")
    print(f"time: {time} or {time-1200}pm?")
    for wing in wings.keys():
        print(f"wing: {wing}") # wing wing, hello? moshi moshi???
        
        for room in wings[wing].keys():
            bad_room = False
            if not (day in wings[wing][room]):
                # print(f"    oh shit! {room} is just always open on {day}")
                continue
            for i, timeSlot in enumerate(wings[wing][room][day]):
                if not (wings[wing][room][day][i][1] < time):
                    bad_room = True # idk how else to do this
                    break
        if not bad_room:
            print(f"    {room} is open for the rest of the day")
                

def convert_time(raw_time):
    if len(str(raw_time)) == 3:
        return 60 * int(str(raw_time)[0]) + int(str(raw_time)[1:3])
    elif len(str(raw_time)) == 4:
        return 60 * int(str(raw_time)[0:2]) + int(str(raw_time)[2:4])
    else:
        print("bro what what other times do we have")
        return 0


        
main()

code.interact(local = locals())
