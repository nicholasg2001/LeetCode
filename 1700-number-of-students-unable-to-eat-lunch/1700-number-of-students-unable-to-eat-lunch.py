class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = sum(students) # Number of students prefer to eat square sandwich (sandwich 1)
        zeros = len(students) - ones # Number of students prefer to eat circle sandwich (sandwich 0)
        for s in sandwiches:
            if s == 1: # If sandwich 1 at top of stack
                if ones == 0: # And NO student who prefers sandwich 1 anymore -> NOT a single student can take the sandwich 1 at top of stack
                    return zeros # Then students who prefer sandwich 0 can't have their lunch
                ones -= 1 # If there're still students who prefer sandwich 1 then those students can take the sandwich at top of stack
            else: # If sandwich 0 at top of stack
                if zeros == 0: # And NO one can take sandwich 0 at top of stack -> sandwiches 1 (if exist in stack but not at top) CANNOT be taken also
                    return ones # Then students who prefer sandwich 1 can't have their lunch
                zeros -= 1 # If there're still students who prefer sandwich 0 then those students can take the sandwich at top of stack
        return 0 # No student has to suffer from starving