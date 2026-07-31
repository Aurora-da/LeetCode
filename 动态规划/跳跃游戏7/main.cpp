#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

class Solution{
public:
	bool canReach(string s, int minJump, int maxJump){
		int n = s.size();
		vector<int> j(n, 0), pre(n, 0);
		j[0] = 1;
		
		for(int i=0; i<minJump; i++){
			pre[i] = 1;
		}
		
		for(int i=minJump; i<n; i++){
			int l = i-maxJump, r = i-minJump;
			if(s[i]=='0'){
				int total = pre[r] - (l <= 0 ? 0:pre[l-1]);
				j[i] = (total!=0);
			}
			pre[i] = pre[i-1] + j[i];
		}
		
		return j[n-1];
	}	
};

int main(){
	
	
	
	return 0;
} 
