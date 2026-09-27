class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = []
        for i in range(len(accounts)):
            parent.append(i)

        rank = [1] * len(accounts)
        
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x

        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            rank[px] += rank[py]
            return True
        

        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        groups = defaultdict(list)

        for email, account_ids in email_to_account.items():
            root = find(account_ids)
            groups[root].append(email)

        result = []

        for root, emails in groups.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))

        return result

        
            

        