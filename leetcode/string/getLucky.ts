function getLucky(s: string, k: number): number {
    let str = s.split('').map((char) => {
        return (char.charCodeAt(0) - 96).toString();
    }).join('');
    
    let sum = 0;
    for (let i = 0; i < str.length; i++) {
        sum += parseInt(str[i]);
    }
    
    for (let i = 1; i < k; i++) {
        sum = sum.toString().split('').map((char) => {
            return parseInt(char);
        }).reduce((acc, cur) => {
            return acc + cur;
        });
    }
    
    return sum;
};