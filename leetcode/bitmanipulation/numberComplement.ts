function findComplement(num: number): number {
    // Step 1: Convert number to binary string
    const binary = num.toString(2);

    // Step 2: Flip the bits
    let flipped = '';
    for (let char of binary) {
        flipped += char === '0' ? '1' : '0';
    }

    // Step 3: Convert the flipped binary string back to a number
    return parseInt(flipped, 2);
}