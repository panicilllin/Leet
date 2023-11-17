class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.weight=0

def solution1(arr):
    # Type your solution here 
    if len(arr) < 2:
        return ''
    if len(arr) < 3:
        return 'Left'
    root = TreeNode(arr[0])
    stack = [root]
    i=0
    while i < len(arr):
        next_stack = []
        for node in stack:
            if node.val == -1:
                continue
            i+=1
            print(i)
            if i >= len(arr):
                continue
            left_node = TreeNode(arr[i])
            node.left =  left_node
            next_stack.append(left_node)
            i+=1
            if i >= len(arr):
                continue
            right_node = TreeNode(arr[i])
            node.right =  right_node
            next_stack.append(right_node)
        stack = next_stack
    
    res = cal_weight(root)
    print(res,root.left.weight, root.right.weight)
    if root.right.weight > root.left.weight:
        return 'Right'
    elif root.right.weight < root.left.weight:
        return 'Left'
    else:
        return ''
    
def cal_weight(node):
    if not node:
        return 0
    if node.val == -1:
        return 0
    left_weight = cal_weight(node.left)
    right_weight = cal_weight(node.right)
    node.weight = left_weight + right_weight + node.val
    return node.weight

    

def solution2(numbers):
    # Type your solution here
    res=0
    for i in numbers:
        res = max(res, i)
    return res

def solution(prices):
    # Type your solution here
    if len(prices) <2:
        return 0
    max_profit=0
    for buy_time in range(0,len(prices)-1):
        for sell_time in range(buy_time+1,len(prices)):
            profit = prices[sell_time] - prices[buy_time]
            max_profit = max(profit,max_profit)
    return max_profit


if __name__ == "__main__":
    a = solution([6, 0, -1, 10])
    print(a)
    

        
    
        