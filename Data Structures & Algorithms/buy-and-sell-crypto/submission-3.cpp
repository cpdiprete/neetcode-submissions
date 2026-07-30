class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 
        int maxSeen = 0;
        size_t head = 0;
        size_t tail = 0;
        while (tail < prices.size()) {
            int currentProfit = prices[tail] - prices[head];
            if (currentProfit > maxSeen) {
                maxSeen = currentProfit;
            }

            if (prices[tail] < prices[head]) {
                head = tail;
            }
            // when should I move which of them forward?
            tail++;
            
        }
        return maxSeen;
        
    }
};
