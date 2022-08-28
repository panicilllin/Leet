from typing import List


class Solution1:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] < diff:
                    continue
                elif nums[j] - nums[i] > diff:
                    break
                else:
                    for k in range(j + 1, len(nums)):
                        if nums[k] - nums[j] < diff:
                            continue
                        elif nums[k] - nums[j] == diff:
                            res += 1
                        else:
                            break
        return res


class Solution2:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        nodes = {node: [] for node in range(0, n)}
        nodes = self.build_tree(0,edges,nodes,restricted)
        # print(nodes)
        # res = self.find_node(nodes,0)
        # print(res)
        res = 1
        for i in nodes.values():
            res+=len(i)
        return res


    def build_tree(self,root,edges,nodes,restricted):
        trashbin = []
        for i in range(len(edges)):
            edge = edges[i]
            if root in edge:
                trashbin.append(i)
                son_node = edge[0] if edge[0]!=root else edge[1]
                if son_node not in restricted:
                    nodes[root].append(son_node)
        for trash in reversed(trashbin):
            del edges[trash]
        # print(root,nodes[root])
        for son_node in nodes[root]:
            nodes = self.build_tree(son_node,edges,nodes,restricted)
        return nodes


class Solution3_false:
    def validPartition(self, nums: List[int]) -> bool:
        last_cut = []
        for i,num in enumerate(nums):
            print(last_cut)
            if not last_cut:
                last_cut.append(num)
            elif len(last_cut)==1:
                if num == last_cut[0]:
                    last_cut.append(num)
                elif num == last_cut[0]+1:
                    last_cut.append(num)
                else:
                    return False
            elif len(last_cut)==2:
                if last_cut[0]==last_cut[1]:#[a,a]
                    if num != last_cut[1]:#[a,a,x]
                        last_cut = [num]
                    else:# [a,a,a]
                        last_cut.append(num)
                elif last_cut[1]==last_cut[0]+1: #[1,2]
                    if num==last_cut[1]+1: # [1,2,3]
                        last_cut = []
                    else:
                        return False
                else: # [1,n] not suppose to show
                    print(f"---------")
                    return False
            elif len(last_cut)==3:
                if num == last_cut[2]+1:
                    last_cut = [last_cut[2],num]
                elif num == last_cut[2]:
                    last_cut.append(num)
                else:
                    last_cut = [num]
            elif len(last_cut)==4:
                if num== last_cut[-1]:
                    continue
                elif num == last_cut[-1]+1:
                    last_cut = [last_cut[-1],num]
                else:
                    last_cut = [num]
        print(last_cut)
        if len(last_cut)==1:
            return False
        if len(last_cut)==2:
            if last_cut[0] != last_cut[1]:
                return False

        return True

    class Solution:
        def validPartition(self, nums: List[int]) -> bool:
            if len(nums)<2:
                return False
            elif len(nums)==2:
                if nums[0]!=nums[1]:
                    return False
                return True

            for i in range(2,len(nums)):
                past

if __name__ == "__main__":
    a = Solution()
    b = a.validPartition(nums = [783377,783378,783379,783380,783381,783382,783383,783384,783385,783386,783387,783388,14925,14925,14925,190887,190887,190887,444668,444668,444668,444668,444669,444670,444671,444672,444673,444674])
    print(b)