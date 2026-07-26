class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // head and tail, if head + tail > target decrement head, otherwise tail if this isn't target
        int head = 0;
        int tail = (int) numbers.size() - 1;
        while (head < tail) {
            int front = numbers[head];
            int back = numbers[tail];
            if ((front + back) == target) {
                vector<int> returned;
                returned.push_back((int) head + 1); // bc they're 1 indexed
                returned.push_back((int) tail + 1);
                return returned;
                // std::vector([head, tail]); // This is gonig to fail
            }
            if ((front + back) > target) {
                // back too big
                tail--;
                continue;
            }
            head++;
        }
        return std::vector<int>();
    }
};
