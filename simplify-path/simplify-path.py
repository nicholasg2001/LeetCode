class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        new_path = path.split("/")

        for c in new_path:

            if c == "..":
                if stack:
                    stack.pop()
            
            else:
                if c and c != ".":
                    stack.append(c)

        return "/" + "/".join(stack)