package _053_Maximum_Subarray

// kadane
func maxSubArray(nums []int) int {
	gsum := nums[0]
	local := 0
	for _, num := range nums[:] {
		local += num
		if local > gsum {
			gsum = local
		}
		if local < 0 {
			local = 0
		}
	}
	return gsum
}
