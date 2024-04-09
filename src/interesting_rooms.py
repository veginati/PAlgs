import heapq


class Room:
    def __init__(self, room_id: int, duration: int, end_time: int):
        self.room_id = room_id
        self.duration = duration
        self.end_time = end_time

    def __lt__(self, other):
        if self.end_time == other.end_time:
            return self.room_id < other.room_id
        return self.end_time < other.end_time


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if n == 1:
            return 0
        # sort meetings in increasing order of start_time
        meetings.sort(key=lambda x: x[0])
        # print(meetings)
        rooms_count = [0 for _ in range(n)]
        rooms_heap = []
        available_rooms = []
        for i in range(n):
            heapq.heappush(available_rooms, i)

        for meeting in meetings:
            while len(rooms_heap) > 0 and rooms_heap[0].end_time <= meeting[0]:
                avaiable_room = heapq.heappop(rooms_heap)
                heapq.heappush(available_rooms, avaiable_room.room_id)

            if len(available_rooms) > 0:
                first_room = heapq.heappop(available_rooms)
                avaiable_room = Room(first_room, meeting[1] - meeting[0] + 1, meeting[1])
                rooms_count[first_room] += 1
                heapq.heappush(rooms_heap, avaiable_room)
            else:
                avaiable_room = heapq.heappop(rooms_heap)
                rooms_count[avaiable_room.room_id] += 1
                avaiable_room.end_time = avaiable_room.end_time + meeting[1] - meeting[0]
                avaiable_room.end_time = max(avaiable_room.end_time, meeting[1])
                heapq.heappush(rooms_heap, avaiable_room)

        max_usage, max_usage_index = -1, -1
        # print(rooms_count)
        for i in range(n):
            if rooms_count[i] > max_usage:
                max_usage_index = i
                max_usage = rooms_count[i]

        return max_usage_index


