from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        # email -> first account index that owns this email
        email_to_account = {}

        # 1. Union accounts that share an email
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        # 2. Group emails by their account root
        groups = defaultdict(list)

        for email, account_idx in email_to_account.items():
            root = find(account_idx)
            groups[root].append(email)

        # 3. Build result
        result = []

        for root, emails in groups.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))

        return result