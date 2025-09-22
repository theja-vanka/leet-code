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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* dummyHead = new ListNode();
        ListNode* dummy = dummyHead;
        int carry = 0;
        int temp;

        while(l1 != nullptr || l2 != nullptr || carry != 0){
            int v1 = (l1 != nullptr) ? l1->val : 0;
            int v2 = (l2 != nullptr) ? l2->val : 0;

            temp = v1 + v2 + carry;
            dummy->next = new ListNode(temp % 10);
            carry = int(temp / 10);

            dummy = dummy->next;
            if(l1 != nullptr){
                l1 = l1->next;
            }
            if(l2 != nullptr){
                l2 = l2->next;
            } 
        }

        return dummyHead->next;
    }
};