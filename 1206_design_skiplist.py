import random


class SkipNode:
    def __init__(self, val=-1):
        self.val = val
        self.next = [None]*4


class Skiplist:

    def __init__(self):
        self.level_count = 1
        self.max_level = 4
        self.head = SkipNode(-1)
        self.head.next = [None]*self.max_level

    def rand_level(self, p=0.5):
        level = 1
        while random.random() < p and level < self.max_level:
            level += 1
        return level

    def search(self, target: int) -> bool:
        level = self.rand_level()

        p = self.head
        self.print_node('ser',target)
        if p.val == target:
            return True
        for i in range(level-1, -1, -1):
            while p.next[i] is not None and p.next[i].val < target:
                p = p.next[i]
            if p.next[i] and p.next[i].val == target:
                return True
        return False

    def add(self, num: int) -> None:
        level = self.rand_level()
        self.level_count = max(level, self.level_count)
        new_node = SkipNode(val=num)
        # new_node.next = [None] * level
        update = [self.head] * level

        p = self.head
        for i in range(level - 1, -1, -1):
            while p.next[i] and p.next[i].val <= num:
                p = p.next[i]
            update[i] = p

        for i in range(level):
            new_node.next[i] = update[i].next[i]  # new_node.next = prev.next
            update[i].next[i] = new_node  # prev.next = new_node
        self.print_node('add',num)

    def erase(self, num: int) -> bool:
        level = self.rand_level()
        new_node = SkipNode(val=num)
        new_node.next = [None] * level
        update = [None] * self.level_count
        p = self.head
        pre_p = p
        for i in range(self.level_count-1, -1, -1):
            while p.next[i] is not None and p.next[i].val < num:
                pre_p = p
                p = p.next[i]
            if p.next[0] and p.next[0].val == num:
                while p.next[0] and p.next[0].val == num:
                    pre_p = p
                    p = p.next[0]
            update[i] = pre_p

        if p.val == num:
            for i in range(len(update)-1,-1, -1):
                if update[i].next[i] and update[i].next[i].val == num:
                    update[i].next[i] = update[i].next[i].next[i]
            self.print_node('era',num)
            return True
        else:
            self.print_node('era',num)
            return False

    def print_node(self,cmd,val):
        # return
        p = self.head
        vals = [cmd+'-'+str(val), p.val]
        while p.next[0]:
            p = p.next[0]
            vals.append(p.val)
        print(vals)



# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)


if __name__ == "__main__":

    cmd =["Skiplist","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","search","add","erase","search","erase","search","erase","erase","erase","add","erase","add","search","erase","search","add","erase","erase","erase","add","erase","erase","add","erase","add","erase","search","erase","search","search","erase","search","search","add","erase","search","search","erase","search","add","add","search","erase","search","search","search","add","search","add","add","add","add","search","erase","add","search","add","search","erase","add","add","add","erase","search","search","search","add","add","erase","add","erase","add","search","add","search","search","search","search","erase","add","erase","search","search","search","search","erase","search","erase","add","add","add","search","erase","search","search","add","add","erase","add","erase","search","erase","search","erase","add","search","search","search","search","search","search","search","search","search","search","search","search","search","search","search"]
    cmd_val = [[],[22],[25],[0],[11],[8],[1],[22],[3],[26],[15],[14],[3],[28],[17],[26],[21],[20],[11],[2],[17],[14],[9],[24],[13],[10],[29],[4],[25],[28],[7],[8],[29],[2],[9],[0],[23],[2],[3],[6],[9],[26],[1],[18],[13],[0],[15],[18],[7],[2],[9],[22],[1],[12],[13],[12],[15],[4],[19],[14],[21],[6],[3],[8],[1],[24],[1],[26],[27],[0],[21],[16],[27],[22],[23],[28],[5],[2],[9],[16],[1],[16],[23],[8],[5],[6],[19],[6],[27],[0],[21],[26],[5],[14],[25],[24],[21],[4],[21],[28],[25],[28],[23],[8],[27],[24],[1],[8],[17],[4],[21],[4],[19],[8],[23],[4],[11],[22],[25],[6],[9],[28],[11],[8],[25],[6],[5],[18],[29],[20],[15],[2],[3],[26],[15],[6]]
    
    res = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,False,None,True,False,True,True,False,False,False,None,False,None,True,True,False,None,False,False,False,None,False,False,None,False,None,True,True,False,False,True,True,False,False,None,True,True,True,False,False,None,None,True,False,True,False,False,None,True,None,None,None,None,False,True,None,False,None,True,False,None,None,None,False,False,True,False,None,None,True,None,False,None,True,None,True,True,False,True,True,None,True,True,False,True,False,True,True,True,None,None,None,True,False,True,False,None,None,True,None,True,False,True,False,True,None,False,False,True,False,True,False,False,False,True,True,True,True,True,True,True]


    c = Skiplist()

    for i in range(1, len(cmd)):
        res_1 = None
        if cmd[i] == 'add':
            c.add(cmd_val[i][0])

        elif cmd[i] == 'search':
            res_1 = c.search(cmd_val[i][0])

        elif cmd[i] == 'erase':
            res_1 = c.erase(cmd_val[i][0])
        print(res[i], res_1)
        if res_1 != res[i]:
            print(i)
            break

# NO AC