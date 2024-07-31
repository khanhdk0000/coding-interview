class LFUCache {
  private capacity: number;
  private cache: {
    key: number;
    value: number;
    frequency: number;
  }[];
  constructor(capacity: number) {
    this.capacity = capacity;
    this.cache = new Array();
  }

  get(key: number): number {
    let index = this.cache.findIndex((x) => x.key === key);
    if (index === -1) {
      return -1;
    }
    // Take the element out and put it back in
    let element = this.cache[index];
    this.cache.splice(index, 1);
    element.frequency++;
    this.cache.push(element);
    return element.value;
  }

  put(key: number, value: number): void {
    if (this.cache.length >= this.capacity) {
      let min = Math.min(...this.cache.map((x) => x.frequency));
      // Get the least used element
      // find last index
      let indexLeastUsed = this.cache.findIndex((x) => x.frequency === min);
      this.cache.splice(indexLeastUsed, 1);
    }
    let index = this.cache.findIndex((x) => x.key === key);
    if (index === -1) {
      this.cache.push({
        key: key,
        value: value,
        frequency: 1,
      });
    } else {
      // Take the element out and put it back in
      let element = this.cache[index];
      this.cache.splice(index, 1);
      element.frequency++;
      this.cache.push(element);
    }
  }
}
