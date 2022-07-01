class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        simplePath = []

        end = start = 1
        while end < len(path):
            while end < len(path) and path[end] != "/":
                end += 1
            if path[start:end] != ".." and path[start:end] != "." and start != end:
                stack.append([start, end])
            elif path[start:end] == ".." and stack:
                stack.pop()
            end += 1
            start = end

        for i in range(len(stack)):
            simplePath.append(None)

        idx = len(simplePath) - 1
        while stack:
            start, end = stack.pop()
            simplePath[idx] = [start, end]
            idx -= 1

        newPath = ["/"]
        for i in range(len(simplePath)):
            file = []
            startIdx = simplePath[i][0]
            endIdx = simplePath[i][1]
            for char in range(startIdx, endIdx):
                file.append(path[char])
            newPath.append("".join(file))
            if i != len(simplePath) - 1:
                newPath.append("/")

        return "".join(newPath)