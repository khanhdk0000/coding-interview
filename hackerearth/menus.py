def solve(menus):
    """1-indexed menu with most column-max prices, tiebreak on higher sum."""
    col_max = [max(col) for col in zip(*menus)]

    best_score = None
    best_menu = 0
    for i, menu in enumerate(menus, start=1):
        good = sum(price == col_max[j] for j, price in enumerate(menu))
        score = (good, sum(menu))
        if best_score is None or score > best_score:
            best_score = score
            best_menu = i
    return best_menu


n, m = map(int, input().split())
menus = [list(map(int, input().split())) for _ in range(n)]

out_ = solve(menus)
print(out_)
