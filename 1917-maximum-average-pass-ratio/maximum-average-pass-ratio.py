class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        sum = 0
        A = []
        for p, q in classes:
            sum += p / q
            A.append(((p - q) / (q * (q + 1)), p, q))
        heapify(A)
        for _ in range(extraStudents):
            (r, p, q) = A[0]
            if r == 0:
                break
            sum -= r
            r2 = (p - q) / ((q + 1.0) * (q + 2.0))
            heapreplace(A, (r2, p + 1, q + 1))
        return sum / n