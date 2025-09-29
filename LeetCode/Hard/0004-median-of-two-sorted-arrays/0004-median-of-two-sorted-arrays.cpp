class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        vector<int> temp;
        if(nums1.size() > nums2.size()){
            temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        int m = nums1.size();
        int n = nums2.size();

        int low = 0;
        int high = m;
        double num1Left, num2Left, num1Right, num2Right;
        while(low<=high){
            int i = (low+high)/2;
            int j = (m+n+1)/2-i;

            if(i==0){
                num1Left = -numeric_limits<double>::infinity();
            } else {
                num1Left = nums1[i-1];
            }

            if (j==0){
                num2Left = -numeric_limits<double>::infinity();
            } else {
                num2Left = nums2[j-1];
            }

            if(i==m){
                num1Right = numeric_limits<double>::infinity();
            } else {
                num1Right = nums1[i];
            }

            if (j == n){
                num2Right = numeric_limits<double>::infinity();
            } else {
                num2Right = nums2[j];
            }

            if(num1Left<=num2Right && num2Left<=num1Right){
                if((m+n)%2==0){
                    double med = (max(num1Left, num2Left)+min(num1Right, num2Right))/2;
                    return med; 
                } else {
                    double med=max(num1Left, num2Left);
                    return med;
                }
            } else if(num1Left>num2Right){
                high = i-1;
            } else {
                low = i+1;
            }   
        }
        return -1;
    }
};