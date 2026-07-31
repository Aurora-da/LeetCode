#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	bool canReach(vector<int>& arr, int start){
		vector<bool> visited(arr.size(), false); 
		return dfs(arr, start, visited);
	}
	
	bool dfs(vector<int>& arr, int start, vector<bool>& visited){
		if(start<0 || start>=arr.size()){
			return false;
		}
		
		// 已经访问过，防止无限循环 
		if(visited[start]==true){
			return false;
		}
		
		// 找到结果返回 
		if(arr[start]==0){
			return true;
		}
		
		visited[start] = true;
		
		int left = start-arr[start];
		int right = start+arr[start];
		
		return dfs(arr, left, visited) || dfs(arr, right, visited);
	} 
};

int main(){
	// 指出元素的个数 
	int n;
	cin >> n;
	
	// 储存元素 
	vector<int> arr(n, 0);
	for(int i=0; i<n; i++){
		cin >> arr[i];
	}
	
//	for(int i=0; i<n; i++){
//		cout << arr[i] << " ";
//	} 
	
	// 开始查询位置 
	int start;
	cin >> start;
	
	// 创建查询对象 
	Solution s;
	bool ans = s.canReach(arr, start);
	
	if(ans){
		cout << "可以到达。";
	}
	else{
		cout << "不可以到达。";
	}
	
	return 0;
} 
