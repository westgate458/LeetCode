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
        
        ListNode* pt = head;
        ListNode* pr = nullptr;  
        ListNode* nt = nullptr;  
            
        while (pt!=nullptr) {
            nt = pt->next;
            pt->next = pr;
            pr = pt;
            pt = nt;            
        }
        
        return(pr);
    }
};