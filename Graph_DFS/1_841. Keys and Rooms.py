# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key = [0]
        # 使用集合更合适
        visited = set()
        def enter(rooms, key):
            if key:
                current_key = key.pop()
                if current_key not in visited:
                    visited.add(current_key)
                    # visited.append(current_key)
                    key.extend(rooms[current_key])
                enter(rooms, key)
            return visited
        return len(enter(rooms, key)) == len(rooms)
            
            