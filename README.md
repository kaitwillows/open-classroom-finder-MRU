# progress:
this project is very much a work in progress, it is not functional yet

the following is a list of things that need to get done:
- [x] pre-processing part 1 
    - [ ] script/automated method for obtaining jsons from mtroyal.ca
    - [x] recursively scrape data into a python dictionary tree
        - [x] include/concatenate multiple files
    - [x] write relevant information to new .json file
    - [ ] create a .json file written in terms of room numbers, using the .json file which is written in terms of class sections
    - current limitations:
        - the structure is rigid: any changes to the structure of the json data provided by mtroyal.ca will break this. i don't think this can be addressed
        - for sake of simplicity, everything is a dictionary. all lists are translated using a globa_i index for the keys, ensuring no repeats. this isn't the best way to do this
        - no batching: data for all ~2500 sections is loaded into memory at once, however, the data is only around 8.0mb, so it's easily manageable on modern systems


- [ ] cli program
    - the best way to do this might be a class/object structure, where each room can tell you if it is open or not, or how long till it will be booked
    - [ ] "when is this class open till?"
    - [ ] "which classrooms in this wing/building/floor will be open for the longest"
    - [ ] maybe: getting more info on room schedule
- [ ] clean up/making repo public
    - [ ] code clean up
    - [ ] documentation
    - [ ] remove class list jsons
        - while this data is [publicly avalable](https://ban9ssb-prod.mtroyal.ca/StudentRegistrationSsb/ssb/term/termSelection?mode=search), it would be better to have a user-side script handle the retrieving of the data.




