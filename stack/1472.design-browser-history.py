#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class BrowserHistory:
    '''
    two index variables to keep track of current index in history
    and the maximum limit in the history.

    every time we visit a new url, increment the curr index, and append it to the history list if curr == len(history).
    otherwise, we set history[curr] = url

    history = [homepage]
    curr = 0
    limit = 0

    back()
    forward()
    '''

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = self.limit = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            # if curr index is most up to date with history list
            self.history.append(url)
        else:
            # if we've went back a few steps, it is safe to be overriding the items going forward.
            self.history[self.curr] = url
        self.limit = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.limit)
        return self.history[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# @lc code=end


operations = ["BrowserHistory", "visit", "visit", "visit", "back",
              "back", "forward", "visit", "forward", "back", "back"]
urls = ["leetcode.com", "google.com",
        "facebook.com", "youtube.com", "linkedin.com"]

steps = [1, 1, 1, 2, 2, 7]
# urls = ['leetcode', 'kolding', 'camping', 'lantern', 'wood']
obj = BrowserHistory(urls[0])
obj.visit(urls[1])
obj.visit(urls[2])
obj.visit(urls[3])

op0 = obj.back(steps[0])
op1 = obj.back(steps[1])
op2 = obj.forward(steps[2])

obj.visit(urls[4])

op3 = obj.forward(steps[3])
op4 = obj.back(steps[4])
op5 = obj.back(steps[5])

print(f'op5: {op5}')
