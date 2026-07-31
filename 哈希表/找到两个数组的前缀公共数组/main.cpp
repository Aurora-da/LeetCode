#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

class Solution{
public:
	vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B){
		int n = A.size();
		unordered_set<int> dataA, dataB;
		unordered_set<int> common;
		vector<int> ans;
		
		for(int i=0; i<n; i++){
			dataA.emplace(A[i]);
			dataB.emplace(B[i]);
			if(dataA.count(B[i])){
				common.emplace(B[i]);
			}
			if(dataB.count(A[i])){
				common.emplace(A[i]);
			}
			ans.push_back(common.size());
		}
		return ans;
	}
};

int main(){
	int n;
	cin >> n;
	
	Solution s;
	vector<int> A(n);
	vector<int> B(n);
	
	for(int i=0; i<n; i++){
		cin >> A[i];
	}
	
	for(int i=0; i<n; i++){
		cin >> B[i];
	}
	
	vector<int> ans = s.findThePrefixCommonArray(A, B);
	
	for(int i=0; i<ans.size(); i++){
		cout << ans[i] << " ";
	}
	
	return 0;
}
