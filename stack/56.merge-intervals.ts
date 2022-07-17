const merge = (intervals: number[][]): number[][] => {
  const stack: number[][] = [];
  intervals.sort((a, b) => (a[0] <= b[0] ? -1 : 1));
  for (let curr of intervals) {
    if (stack.length && curr[0] <= stack[stack.length - 1][1]) {
      // [a, b]
      stack[stack.length - 1][1] = Math.max(
        stack[stack.length - 1][1],
        curr[1]
      );
    } else {
      stack.push(curr);
    }
  }
  return stack;
};

let intervals = [
  [1, 3],
  [2, 6],
  [8, 10],
  [15, 18],
];
intervals = [
  [1, 4],
  [4, 5],
];

const ans = merge(intervals);
console.log('ans', ans);
