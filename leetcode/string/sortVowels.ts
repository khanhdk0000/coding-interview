function sortVowels(s: string): string {
  const vowels = ["a", "e", "i", "o", "u"];
  const upperCaseVowels = ["A", "E", "I", "O", "U"];
  const strLowerVowels = s
    .split("")
    .filter((c) => vowels.includes(c))
    .sort((a, b) => a.localeCompare(b));
  const strUpperVowels = s
    .split("")
    .filter((c) => upperCaseVowels.includes(c))
    .sort((a, b) => a.localeCompare(b));
  const sortedVowels = [...strUpperVowels, ...strLowerVowels];

  let result = "";
  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i]) || upperCaseVowels.includes(s[i])) {
      result += sortedVowels.shift();
    } else {
      result += s[i];
    }
  }
  return result;
}
