class Solution {

public:
    int search(vector<int>& nums, int target) {
        int end = nums.size() - 1;
        int start = 0;
        while (start <= end) {
            // std::cout << (start + end) << std::endl;
            int mid = (start + end) / 2; // C++ int division truncates
            if (nums[mid] < target) {
                // need to move up
                start = mid + 1; 
                continue;
            } else if (nums[mid] > target) {
                end = mid - 1;
                continue;
            } else {
                return mid;
            }
        }   
        return -1; 
    }
};
