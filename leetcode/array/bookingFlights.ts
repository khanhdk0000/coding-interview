function corpFlightBookings(bookings: number[][], n: number): number[] {
    let bookSeats = new Array(n).fill(0);
    for (let i = 0; i < bookings.length; i++) {
        const [start, end, seats] = bookings[i];
        for (let j = start -1; j < end; j ++) {
            bookSeats[j] += seats;
        }
    }
    return bookSeats;
};