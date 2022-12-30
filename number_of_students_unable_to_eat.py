class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        curr = 0
        while students:
            if(students[0] == sandwiches[0]):
                curr = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                curr += 1
                students.append(students.pop(0))
            if(curr >= len(students)):
                break
        return len(students)
