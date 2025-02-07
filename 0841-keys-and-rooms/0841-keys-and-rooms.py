class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        result = [False] * len(rooms)
        result[0] = True
        keys = rooms[0]
        while keys:
            key = keys.pop()
            if result[key]:
                continue
            result[key] = True
            keys += [k for k in rooms[key] if result[k] is False]

        return all(result)
            
