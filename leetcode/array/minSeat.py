import heapq
class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        order = sorted(range(len(times)), key = lambda x: times[x][0])
        emptySeats, takenSeats = list(range(len(times))), []

        for i in order:
            ar, lv = times[i]

            while takenSeats and takenSeats[0][0] <= ar:
                heapq.heappush(emptySeats, heapq.heappop(takenSeats)[1])
            seat = heapq.heappop(emptySeats)

            if i == targetFriend: return seat

            heapq.heappush(takenSeats,(lv, seat))  