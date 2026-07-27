class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int difference = target - nums[i];
            auto found = seen.find(difference);
            if (found != seen.end()) {
                // Didn't reach the end looking for it, found it!
                return {found->second, i};
            } else {
                seen.emplace(nums[i], i);
            }
            // check if difference in dict, if so return the (seen[difference], i)
            // if not, add seen[nums[i]] = i
        }
    }
};
