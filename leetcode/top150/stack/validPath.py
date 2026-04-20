class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        n = len(path)

        while i < n:
            # Skip consecutive slashes
            while i < n and path[i] == '/':
                i += 1

            # Read the next component
            component = []
            while i < n and path[i] != '/':
                component.append(path[i])
                i += 1

            part = "".join(component)

            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)

        return "/" + "/".join(stack)