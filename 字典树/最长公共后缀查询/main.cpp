#include<iostream>
#include<vector>
#include<cstring>

using namespace std;

class TrieNode{
public:
	TrieNode* children[26];		// 正好对应着26个英文字母 
	int best_idx;
	
	TrieNode() : best_idx(-1){
		memset(children, 0, sizeof(children));
	}
	
	~TrieNode(){
		for(int i=0; i<26; i++){
			delete children[i];
		}
	}
};

class Solution{
public:
	vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery){
		TrieNode* root = new TrieNode();
		
		int global_best_idx = 0;
		for(int i=0; i<wordsContainer.size(); i++){
			if(wordsContainer[i].size() < wordsContainer[global_best_idx].size()){
				global_best_idx = i;
			}
		}
		root->best_idx = global_best_idx;
		
		for(int i=0; i<wordsContainer.size(); i++){
			const string& word = wordsContainer[i];
			TrieNode* node = root;
			
			for(int j=word.size()-1; j>=0; j--){
				int idx = word[j] - 'a';
				if(!node->children[idx]){
					node->children[idx] = new TrieNode();
				}
				node = node->children[idx];
				
				if(node->best_idx==-1 || word.size() < wordsContainer[node->best_idx].size()){
					node->best_idx = i;
				}
			}
		}
		
		vector<int> ans;
		for(const string& query : wordsQuery){
			TrieNode* node = root;
			
			for(int j=query.size()-1; j>=0; j--){
				int idx = query[j] - 'a';
				if(node->children[idx]){
					node = node->children[idx];
				}
				else{
					break;
				}
			}
			ans.push_back(node->best_idx);
		}
		
		delete root;
		
		return ans;
	}
};
