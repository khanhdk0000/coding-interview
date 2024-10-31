function minFrogJump(X: number, Y: number, D: number): number {
    if (X >= Y) {
        return 0;
    }
    return Math.ceil((Y - X) / D);
}
