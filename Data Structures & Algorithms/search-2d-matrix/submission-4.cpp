class Solution {
private:
 bool searchSingleRow(vector<int>& row, int target) {
    std::cout << "Search single row ----------------" << row[0] << std::endl;
    int start = 0;
    int end = row.size() - 1;
    while (start <= end) {
        int mid = (start + end) / 2;
        if (row[mid] > target) {
            end = mid - 1;
            continue;
        } else if (row[mid] < target) {
            start = mid + 1;
            continue;
        } else {
            return true;
        }
    }
    return false;
};
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // start from first element of first row, and last element of last row
        int breakCount = 0;
        // if element > middle
        int start = 0;
        int end = matrix.size() - 1;
        
        while (start <= end) {
            int middle = (start + end) / 2;
            int mMiddleStart = matrix[middle][0]; // I chose to use the smallest element from the middle, I don't think this is an issue?
            int mMiddleEnd = matrix[middle][matrix[middle].size() - 1];

            std::cout << "Start:" << start << "end: " << end << std::endl;
            // if (breakCount > 10) {
            //     return -1;
            // }
            // if (start == end) {
            //     return searchSingleRow(matrix[start], target);
            // }
            // int sStart = matrix[start][0];
            // int eEnd = matrix[end][matrix[end].size() - 1];
            if ((start == end) || (mMiddleStart <= target && mMiddleEnd >= target)) {
                // it's in this row
                return searchSingleRow(matrix[middle], target);
            }
            if (mMiddleStart > target) {
                end = middle - 1;
                continue;
            } else if (mMiddleStart < target) {
                // TODO: need the check the end of this row
                if ((target > matrix[start][0]) && (target < matrix[start][matrix[start].size() - 1])) {
                    return searchSingleRow(matrix[start], target);
                }
                start = middle + 1;
                continue;
            } else {
                return true; // found this element right here
            }
        }
        return false;
    }
};
