def solve(N, start, finish, ticket_cost):
    """Cheaper of the two arcs between start and finish on the circle."""
    a = (start - 1) % N
    b = (finish - 1) % N
    if a == b:
        return 0
    lo, hi = min(a, b), max(a, b)
    one_way = sum(ticket_cost[lo:hi])
    return min(one_way, sum(ticket_cost) - one_way)


N = int(input())
start = int(input())
finish = int(input())
ticket_cost = list(map(int, input().split()))

out_ = solve(N, start, finish, ticket_cost)
print(out_)
