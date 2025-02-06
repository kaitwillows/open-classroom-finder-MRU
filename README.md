# progress:
this project is very much a work in progress, it is not functional yet

the following is a list of things that need to get done:
- [ ] pre-processing
  - pre-processing is needed the raw json files that can be obtained from mymru.ca
  - [x] recursively scrape data into a python dictionary tree
    - [ ] include/concatinate multiple files
  - [ ] translate the tree of class sections and when/where they meet, to a data structre in terms of room numbers and when they're booked
- [ ] cli program
  - [ ] "when is this class open till?"
  - [ ] "which classrooms in this wing/building/floor will be open for the longest"
  - [ ] maybe: getting more info on room schedule
- [ ] clean up/making repo public
  - [ ] code clean up
  - [ ] documentation
  - [ ] remove class list jsons from commit history (maybe not)


# limitations(??)
- since the classroom data is semi-private (only avalable to MRU students), i won't be having it packaged with the code
  - TODO: remove JSON from the commit history before making repo public public (i assume you can do that)
  - WAIT MAYBE IT IS? just go to <https://ban9ssb-prod.mtroyal.ca/StudentRegistrationSsb/ssb/term/termSelection?mode=search>
- as the data only needs to be gathered/preprocessed once per semester, its not imperative that the process be automated
