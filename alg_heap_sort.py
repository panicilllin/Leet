from typing import List


class Solution:

    def heapify(self, arr: List, index: int, heap_size: int) -> List:
        left_child = index * 2 + 1  # 左子节点
        print(f"left child={left_child}")

        while left_child < heap_size:  # 下方有子节点
            print(f"index={index}")
            largest = left_child + 1 \
                if left_child + 1 < heap_size and arr[left_child + 1] > arr[left_child] \
                else left_child  # 判断左右子节点的最大值

            largest = largest if arr[largest] > arr[index] else index  # 判断父子节点的最大值
            print(f"largest={largest}")
            if largest == index:  # 父节点已经是最大值
                break
            # 父节点不是最大值，继续向下走
            print(arr[largest], arr[index])
            arr[largest], arr[index] = arr[index], arr[largest]  # 交换最大值与父节点(确保父节点最大)
            print(arr[largest], arr[index])
            index = largest  # 交换后的子节点设为新的父节点
            left_child = index * 2 + 1  # 新的子节点
            print(left_child)
        return arr

    def hep_insert(self, arr: List, index: int) -> List:
        while arr[index] > arr[int((index - 1) / 2)]:
            father_node = int((index - 1) / 2)
            arr[index], arr[father_node] = arr[father_node], arr[index]
            index = father_node
        return arr

    def heap_sort(self, arr: List):

        if not arr or len(arr) < 2:
            return
        for i in range(0, len(arr)):
            arr = self.hep_insert(arr, i)
            i += 1
        print(arr)
        heap_size = len(arr)-1
        arr[0], arr[heap_size] = arr[heap_size], arr[0]
        while heap_size > 0:
            arr = self.heapify(arr, 0, heap_size)
            heap_size -= 1
            arr[0], arr[heap_size] = arr[heap_size], arr[0]
        return arr


if __name__ == "__main__":
    a = Solution()
    b = a.heap_sort(arr=[3, 0, 2, 5, 4, 9, 1, 5, 5, 7, 2, 1])
    print(b)
