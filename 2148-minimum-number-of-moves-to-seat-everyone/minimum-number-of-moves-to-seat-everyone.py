class Solution(object):
    def minMovesToSeat(self, seats, students):
        total = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            if seats[i] != students[i]:
                total += abs(seats[i]-students[i])

        return total