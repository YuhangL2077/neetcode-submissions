class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        indegree = {}
        for word in words:
            for c in word:
                graph[c] = set()
        for word in words:
            for c in word:
                indegree[c] = 0
        # build graph
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_len = min(len(word1), len(word2))
        
        # invalid prefix case
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""

            for j in range(min_len):
                c1 = word1[j]
                c2 = word2[j]

                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break
        # topo sort
        q = deque()

        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        ans = []

        while q:
            char = q.popleft()
            ans.append(char)

            for nei in graph[char]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
        if len(ans) != len(indegree):
            return ""
        return "".join(ans)


