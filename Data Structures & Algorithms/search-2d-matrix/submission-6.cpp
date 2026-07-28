class Solution {
private:
 bool searchSingleRow(vector<int>& row, int target) {
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

            if ((start == end) || (mMiddleStart <= target && mMiddleEnd >= target)) {
                // it's in this row
                return searchSingleRow(matrix[middle], target);
            }
            if (mMiddleStart > target) {
                end = middle - 1;
                continue;
            } else if (mMiddleStart < target) {
                start = middle + 1;
                continue;
            } else {
                return true; // found this element right here
            }
        }
        return false;
    }
};
