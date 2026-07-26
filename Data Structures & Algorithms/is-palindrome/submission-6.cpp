class Solution {
public:
    bool isPalindrome(string s) {
        size_t start = 0;
        size_t end = s.length() - 1;
        while (start < end) {
            if (!(std::isalnum(s[start]))) {
                start++;
                continue;
            }
            if (!(std::isalnum(s[end]))) {
                end--;
                continue;
            }
            char head = std::tolower(s[start]);
            char tail = std::tolower(s[end]);
            if (head != tail) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};
