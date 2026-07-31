#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	int search(vector<int>& nums, int target){
		int n = nums.size();
		int l = 0;
		int r = n-1;
		
		if(!n){
			return -1;
		}
		
		if(r==1){
			return nums[0]==target ? 0:-1;
		}
		
		while(l <= r){
			int mid = (l+r)/2;
			
			if(nums[mid] == target){
				return mid;
			}
			
			if(nums[0]<=nums[mid]){
				if((nums[0]<=target) && (target<nums[mid])){
					r = mid-1;
				}
				else{
					l = mid+1;
				}
			}
			else{
				if((nums[mid]<target) && (target<=nums[n-1])){
					l = mid+1;
				}
				else{
					r = mid-1;
				} 
			}
		}
		
		return -1;
	}
};

int main(){
	int n;
	cin >> n;
	
	vector<int> nums(n, 0);
	for(int i=0; i<n; i++){
		cin >> nums[i];
	}
	
	int target;
	cin >> target;
	
	Solution s;
	int ans = s.search(nums, target);
	cout << ans;
	
	return 0;
}
