class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        for i in range(len(s)):
            mini = float("inf")
            for j in range(len(s)):
                if s[j] == c:
                    val = abs(i - j)
                    mini = min(val, mini)
            answer.append(mini)

        return answer

        