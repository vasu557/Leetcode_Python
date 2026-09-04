class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int>maxarray(n,0);
        vector<int>minarray(n,0);
        int maxi = INT_MIN;
        int mini = INT_MAX;
        for(int i=0;i<nums.size();i++){
            if(nums[i] > maxi ){
                maxi = nums[i];
            }
            maxarray[i] = maxi;
        }
        for(int i=n-1;i>=0;i--){
            if(nums[i] < mini){
                mini = nums[i];
            }
            minarray[i] = mini;
        }

        for(int i=0;i<n;i++){
            if(maxarray[i] - minarray[i] <= k){
                return i;
            }
        }
        return -1;
    }
};