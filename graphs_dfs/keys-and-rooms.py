class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.rooms_visited = set()
        self.visit_rooms(0, rooms)
        #print(self.rooms_visited)
        return len(self.rooms_visited) == len(rooms)
        
    def visit_rooms(self, room_index, rooms):
        if room_index in self.rooms_visited:
            return
        self.rooms_visited.add(room_index)
        for i in rooms[room_index]:
            if i not in self.rooms_visited:
                self.visit_rooms(i, rooms)
