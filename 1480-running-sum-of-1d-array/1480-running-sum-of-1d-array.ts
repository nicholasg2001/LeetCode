function runningSum(nums: number[]): number[] {
    
    var runningSum: number = 0
    var sums:number[] = []
    
    for(var index in nums){
        runningSum = runningSum + nums[index];
        sums.push(runningSum);
    }
    return sums;
};