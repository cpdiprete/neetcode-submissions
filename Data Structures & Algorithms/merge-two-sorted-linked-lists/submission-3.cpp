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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* newHead = nullptr;
        ListNode* looper = nullptr;
        if (list1 && list2) {
            if (list1->val > list2->val) {
                newHead = list2;
                list2 = list2->next;
            } else {
                newHead = list1;
                list1 = list1->next;
            }
        } else if (list1) {
            newHead = list1;
            list1 = list1->next;
        } else if (list2) {
            newHead = list2;
            list2 = list2->next;
        }
        looper = newHead;
        // std::cout << "start first loop" << std::endl;
        while (list1 && list2) {
            if (list1->val > list2->val) {
                looper->next = list2;
                list2 = list2->next;
            } else {
                // to get here, list1 was bigger
                looper->next = list1;
                list1 = list1->next;
            }
            looper = looper->next;
        }
        // std::cout << "broke first loop" << std::endl;
        while (list1) {
            looper->next = list1;
            list1 = list1->next;
            looper = looper->next;
        }
        while (list2) {
            looper->next = list2;
            list2 = list2->next;
            looper = looper->next;
        }
        return newHead;
    }
};
