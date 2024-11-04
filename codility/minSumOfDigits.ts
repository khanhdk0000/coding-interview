function solution(A: number[]): number {
    const N = A.length;
    let totalSum = 0;

    let maxReduceOne = -1;
    let idxMaxReduceOne = -1;
    let secondmaxReduceOne = -1;
    let idxSecondReduceOne = -1;
    let maxR2 = -1;
    let indexMaxR2 = -1;

    for (let i = 0; i < N; i++) {
        const num = A[i];
        totalSum += num;

        const sumOne = sumOfDigits(num);
        const sumTwo = sumOfDigits(sumOne);

        const reduceOne = num - sumOne;
        const reduceTwo = num - sumTwo;

        // Update maxReduceOne and secondmaxReduceOne
        if (reduceOne > maxReduceOne) {
            secondmaxReduceOne = maxReduceOne;
            idxSecondReduceOne = idxMaxReduceOne;
            maxReduceOne = reduceOne;
            idxMaxReduceOne = i;
        } else if (reduceOne > secondmaxReduceOne) {
            secondmaxReduceOne = reduceOne;
            idxSecondReduceOne = i;
        }

        // Update maxR2
        if (reduceTwo > maxR2) {
            maxR2 = reduceTwo;
            indexMaxR2 = i;
        }
    }

    let option1Reduction = maxR2;

    let option2Reduction = -1;
    if (idxSecondReduceOne !== -1) {
        option2Reduction = maxReduceOne + secondmaxReduceOne;
    }

    let option3Reduction = maxReduceOne;

    let maxReduction = 0;
    if (option1Reduction >= option2Reduction && option1Reduction >= option3Reduction) {
        maxReduction = option1Reduction;
    } else if (option2Reduction >= option1Reduction && option2Reduction >= option3Reduction) {
        maxReduction = option2Reduction;
    } else {
        maxReduction = option3Reduction;
    }

    return totalSum - maxReduction;
}

// Helper function to compute the sum of digits of a number
function sumOfDigits(num: number): number {
    let sum = 0;
    while (num > 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
    }
    return sum;
}
