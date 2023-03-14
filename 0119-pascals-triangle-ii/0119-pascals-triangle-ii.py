class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            list = self.getRow(rowIndex - 1)
            new_list = [1]
            for j in range(1, len(list)):
                new_list.append(list[j] + list[j-1])
            new_list.append(1)
            return new_list