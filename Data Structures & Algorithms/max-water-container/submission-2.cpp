class Solution {
public:
    int maxArea(vector<int>& heights) {
        // head and tail, move them closer based on the smallest of the 2 and area check them
        int head = 0;
        int tail = heights.size() - 1;
        std::cout << tail;
        int maxSeen = 0;
        while (head < tail) {
            std::cout << maxSeen << std::endl;

            int limitingHeight = heights[head];
            if (heights[tail] < limitingHeight) {
                limitingHeight = heights[tail];
            }
            // std::cout << "limiting height" << limitingHeight << std::endl;


            int distance = tail - head;
            // std::cout << "distancae" << distance << std::endl;
            if ((distance * limitingHeight) > maxSeen) {
                maxSeen = distance * limitingHeight;
            }
            if (heights[head] > heights[tail]) {
                tail--;
                continue;
            }
            head++;
        }
        return maxSeen;
    }
};
