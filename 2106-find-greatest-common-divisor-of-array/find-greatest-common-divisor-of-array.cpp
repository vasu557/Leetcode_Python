class Solution {
public:

    int myFunction(int a,int b){

        while(a != 0 && b != 0){

            if(a >= b){
                a = a -b;
            }
            else if(b > a){
                b = b - a;
            }
        }

        return a == 0 ? b : a;
    }
    int findGCD(vector<int>& nums) {
        int maxi = INT_MIN;
        int mini = INT_MAX;
       for(int i=0;i<nums.size();i++){
        if(nums[i] > maxi){
            maxi = nums[i];
        }
        if(nums[i] < mini){
            mini = nums[i];
        }
       }


       int ans  = myFunction(mini,maxi);
        
    return ans;
    }
};