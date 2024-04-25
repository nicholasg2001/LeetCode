function runningSum(nums: number[]): number[] {
     let result: number = 0;
     return nums.map(item => result += item);
};

