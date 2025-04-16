# /****************************************************************
#  *             CODERBYTE CORRECT PATH CHALLENGE                 *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function CorrectPath(str) read the str parameter    *
#  * being passed, which will represent the movements made in a   *
#  * 5x5 grid of cells starting from the top left position. The   *
#  * characters in the input string will be entirely composed     *
#  * of: r, l, u, d, ?. Each of the characters stand for the      *
#  * direction to take within the grid,                           *
#  * for example: r = right, l = left, u = up, d = down. Your goal*
#  * is to determine what characters the question marks should be *
#  * in order for a path to be created to go from the top left of *
#  * the grid all the way to the bottom right without touching    *
#  * previously travelled on cells in the grid.                   *
#  *                                                              *
#  * For example: if str is "r?d?drdd" then your program should   *
#  * output the final correct string that will allow a path to be *
#  * formed from the top left of a 5x5 grid to the bottom right.  *
#  * For this input, your program should therefore return the     *
#  * string rrdrdrdd. There will only ever be one correct path &  *
#  * there will always be at least one question mark within the   *
#  * input string.                                                *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: "???rrurdr?"                                        *
#  * Output 1: dddrrurdrd                                         *
#  *                                                              *
#  * Input 2: "drdr??rrddd?"                                      *
#  * Output 2: drdruurrdddd                                       *
#  ***************************************************************/
DIRS = {
    "u": (-1,  0),
    "d": ( 1,  0),
    "l": ( 0, -1),
    "r": ( 0,  1),
}
TARGET      = (4, 4)
BOARD_SIZE  = 5
def CorrectPath(str):
    n = len(str)

    # stack frames: (idx, x, y, visited_set, path_list)
    stack = [
        (0, 0, 0, {(0, 0)}, [])
    ]

    while stack:
        idx, x, y, visited, path = stack.pop()

        # Finished the whole template?
        if idx == n:
            if (x, y) == TARGET:          # success!
                return "".join(path)
            continue                      # wrong end‑cell → back‑track

        # Determine the concrete choices for this character
        c = str[idx]
        choices = "udlr" if c == "?" else c

        # Iterate in reverse so that the first choice (“natural” order)
        # ends up on top of the stack and is explored first
        for move in reversed(choices):
            dx, dy = DIRS[move]
            nx, ny = x + dx, y + dy

            # 1️⃣ stay inside the 5×5 board
            if not (0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE):
                continue
            # 2️⃣ avoid revisiting a cell
            if (nx, ny) in visited:
                continue

            # 3️⃣ Manhattan‑distance + parity pruning
            remaining = n - idx - 1
            dist      = abs(nx - TARGET[0]) + abs(ny - TARGET[1])
            if dist > remaining:
                continue

            # Push the next frame
            stack.append(
                (
                    idx + 1,
                    nx, ny,
                    visited | {(nx, ny)},        # cheap set copy
                    path + [move],               # cheap list copy
                )
            )

print(CorrectPath("???rrurdr?"))  # dddrrurdrd
print(CorrectPath("drdr??rrddd?"))  # drdruurrdddd