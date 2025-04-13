# /****************************************************************
#  *             CODERBYTE BINARY REVERSAL CHALLENGE              *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function BinaryReversal(str) take the str parameter *
#  * being passed, which will be a positive integer, take its     *
#  * binary representation (padded to the nearest N * 8 bits),    *
#  * reverse that string of bits, and then finally return the new *
#  * reversed string in decimal form. For example: if str is "47" *
#  * then the binary version of this integer is 101111 but we pad *
#  * it to be 00101111. Your program should reverse this binary   *
#  * string which then becomes: 11110100 and then finally return  *
#  * the decimal version of this string, which is 244.            *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: "213"                                               *
#  * Output 1: 171                                                *
#  *                                                              *
#  * Input 2: "4567"                                              *
#  * Output 2: 60296                                              *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 54.6% of users who solved this   *
#  * challenge.                                                   *
#  *                                                              *
#  ***************************************************************/

def BinaryReversal(str):
    num = int(str)
    binary = bin(num)[2:]  # Convert to binary and remove '0b' prefix
    paddedLen = ((len(binary) + 7) // 8) * 8  # Pad to nearest multiple of 8
    print(f"Original binary: {binary}, Padded length: {paddedLen}")
    binary = binary.zfill(paddedLen)  # Pad with leading zeros
    reversedBinary = binary[::-1]  # Reverse the binary string
    decimal = int(reversedBinary, 2)  # Convert back to decimal
    return decimal

print(BinaryReversal("47"))    # Output: 244
print(BinaryReversal("213"))   # Output: 171
print(BinaryReversal("4567"))  # Output: 60296