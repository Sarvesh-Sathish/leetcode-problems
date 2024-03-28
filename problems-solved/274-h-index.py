from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 0 1 3 5 6
        # 0 1 2 3 4
        # 1 2 3 4 5
        # 5 4 3 2 1
        citations.sort()
        for i in range(0, len(citations)):
            if len(citations) - i <= citations[i]:
                return len(citations) - i
        return 0

        # 1 1 3
        # 0 1 2
        # 1 2 3
        # 3 2 1