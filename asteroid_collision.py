# https://leetcode.com/problems/asteroid-collision/
from collections import deque


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        collisions = deque()

        for a in asteroids:
            if not collisions or collisions[-1] < 0 or a > 0:
                collisions.append(a)
            else:
                a_mag = abs(a)
                while True:
                    if not collisions:
                        collisions.append(a)
                        break

                    b = collisions[-1]
                    if (a < 0 and b < 0) or (a > 0 and b < 0):
                        collisions.append(a)
                        break
                    elif a_mag == abs(b):
                        collisions.pop()
                        break
                    elif a_mag < abs(b):
                        break
                    else:
                        collisions.pop()
        return list(collisions)
