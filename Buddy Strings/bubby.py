class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
                        if len(s) != len(goal):
                            return False

                        if s == goal:
                            # Check if there are any repeated characters in s
                            seen = set()
                            for char in s:
                                if char in seen:
                                    return True
                                seen.add(char)
                            return False

                        diff_count = 0
                        diff_positions = []
                        for i in range(len(s)):
                            if s[i] != goal[i]:
                                diff_count += 1
                                diff_positions.append(i)

                            if diff_count > 2:
                                return False

                        return diff_count == 2 and s[diff_positions[0]] == goal[diff_positions[1]] and s[diff_positions[1]] == goal[diff_positions[0]]
