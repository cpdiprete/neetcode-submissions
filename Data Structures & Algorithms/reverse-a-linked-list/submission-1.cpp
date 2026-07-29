/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        ListNode* looper = head;
        ListNode* dummy = nullptr; 
        ListNode* scout;
        while (looper && looper->next != nullptr) {
            std::cout << looper->val << std::endl;
            scout = looper->next;
            looper->next = dummy;
            dummy = looper;
            looper = scout;
        }
        looper->next = dummy;

        std::cout << head->val << std::endl;
        if (head->next) {
             std::cout << head->next->val << std::endl;
        }
        return looper;
    }
};
