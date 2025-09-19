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

        ListNode* dummy = new ListNode();
        ListNode* returnDummy = dummy;
        int carry = 0;
        int quotient, temp;

        while(l1 && l2){
            temp = l1->val + l2->val + carry;
            quotient = temp % 10;
            carry = int(temp / 10);
            dummy->next = new ListNode(quotient);
            dummy = dummy->next;
            l1 = l1->next;
            l2 = l2->next;
        }

        while(l1){
            temp = l1->val + carry;
            quotient = temp % 10;
            carry = int(temp / 10);
            dummy->next = new ListNode(quotient);
            dummy = dummy->next;
            l1 = l1->next;
        }
        while(l2){
            temp = l2->val + carry;
            quotient = temp % 10;
            carry = int(temp / 10);
            dummy->next = new ListNode(quotient);
            dummy = dummy->next;
            l2 = l2->next;
        }

        if(carry != 0){
            dummy->next = new ListNode(carry);
        }
        return returnDummy->next;
    }
};