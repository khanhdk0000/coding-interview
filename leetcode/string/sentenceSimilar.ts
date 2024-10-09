function areSentencesSimilar(sentence1: string, sentence2: string): boolean {
  if (sentence1 === "" || sentence2 === "") {
    return true;
  }
  let longerString = "";
  let shorterString = "";
  if (sentence1.length > sentence2.length) {
    longerString = sentence1;
    shorterString = sentence2;
  } else {
    longerString = sentence2;
    shorterString = sentence1;
  }
  const wordsLonger = longerString.split(" ");
  const wordsShorter = shorterString.split(" ");
  if (wordsLonger[0] !== wordsShorter[0] && wordsShorter.length > 1) {
    return false;
  }
  if (
    wordsLonger[wordsLonger.length - 1] !==
      wordsShorter[wordsShorter.length - 1] &&
    wordsShorter.length > 1
  ) {
    return false;
  }
  if (
    wordsShorter.length === 1 &&
    wordsLonger[0] !== wordsShorter[0] &&
    wordsLonger[wordsLonger.length - 1] !== wordsShorter[0]
  ) {
    return false;
  }
  return areSentencesSimilar(
    wordsLonger.slice(1, wordsLonger.length).join(" "),
    wordsShorter.slice(1, wordsShorter.length).join(" ")
  );
}
