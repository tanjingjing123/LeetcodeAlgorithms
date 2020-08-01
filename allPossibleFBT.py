import treeNode
class solution:
    def allPossibleFBT(self, N):
        if N == 1:
            return [treeNode.TreeNode(0)]
        allTrees = []
        for i in range(1, N, 2):
            leftTrees = self.allPossibleFBT(i)
            rightTrees = self.allPossibleFBT(N - 1 - i)
            for lt in leftTrees:
                for rt in rightTrees:
                    allTrees.append(treeNode.TreeNode(0, lt, rt))
        return allTrees

obj = solution()
N = 7
print(obj.allPossibleFBT(N))