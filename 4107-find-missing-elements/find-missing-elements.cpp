class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        vector<int>result;
        unordered_set<int>st;
        int mini = INT_MAX;
        int maxi  = INT_MIN;
        for(int i=0;i<nums.size();i++){
            st.insert(nums[i]);
            if(nums[i] < mini){
                mini = nums[i];
            }
            if(nums[i] > maxi){
                maxi = nums[i];
            }
        }
        sort(nums.begin(),nums.end());
        int temp = 0;
        for(int i=mini;i<=maxi;i++){
            if(!st.count(i)){
                result.push_back(i);
            }
        }
        return result;
    }
};