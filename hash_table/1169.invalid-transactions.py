#
# @lc app=leetcode id=1169 lang=python3
#
# [1169] Invalid Transactions
#

# @lc code=start
from pprint import pp, pprint
from typing import List


class Solution:
    '''
    a dictionary mapping the times to another dictionary containing:
     {
       name: [array of cities]
     }

    declare an empty array to store the bad ones. => res
    run another for loop.
    1. deconstruct the name/city/time/amount from each txn
    2. if amount > 1000 => add it to `res`.
    3. check for another time wihtin the 60min window.
      - if time2 exists, check if name exists for times[time2].
      - check if times[time2][name][0] != city
      - check if length of times[time2][name] > 1.
    '''

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        times = {}
        res = []
        for txn in transactions:
            s = txn.split(',')
            name, time, amount, city = s
            time, amount = map(int, (time, amount))
            if time not in times:
                times[time] = {
                    name: [city]
                }
            else:
                if name not in times[time]:
                    times[time][name] = [city]
                else:
                    times[time][name].append(city)

        for txn in transactions:
            s = txn.split(',')
            name, time, amount, city = s
            time, amount = map(int, (time, amount))
            if amount > 1000:
                res.append(txn)
                continue
            for t in range(time-60, time+60):
                if t not in times:
                    continue
                if name not in times[t]:
                    continue
                # if city != times[t][name][0] or len(times[t][name]) > 1:
                if city != times[t][name][0]:
                    res.append(txn)
                    break

        return res


# @lc code=end

sol = Solution()
transactions = ["alice,20,800,mtv", "alice,50,100,beijing"]
transactions = ["alice,20,800,mtv", "alice,50,1200,mtv"]
transactions = ["alice,20,800,mtv", "bob,50,1200,mtv"]
transactions = ["alice,20,1220,mtv", "alice,20,1220,mtv"]
transactions = ["alice,20,800,mtv",
                "alice,50,100,mtv", "alice,51,100,frankfurt"]
transactions = ["alice,20,800,mtv", "bob,50,1200,mtv", "alice,20,800,mtv",
                "alice,50,1200,mtv", "alice,20,800,mtv", "alice,50,100,beijing"]

ans = sol.invalidTransactions(transactions)
print(f'ans: {ans}')
