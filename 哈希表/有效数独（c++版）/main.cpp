#include<iostream>
#include<vector>
using namespace std;

class Solution{
	public:
		bool isValidSudoku(vector<vector<char> >& board){
			vector<vector<bool> > cols(9, vector<bool>(9, false));
			vector<vector<bool> > rows(9, vector<bool>(9, false));
			vector<vector<bool> > boxes(9, vector<bool>(9, false));
			
			for(int i=0; i<9; i++){
				for(int j=0; j<9; j++){
					if(board[i][j]=='.'){
						continue;
					}
					
					int num = board[i][j] - '1';
					
					int k = (i/3)*3 + j/3;
					
					if(rows[i][num] || cols[j][num] || boxes[k][num]){
						return false;
					}
					
					rows[i][num] = true;
					cols[j][num] = true;
					boxes[k][num] = true;
				}
			}
			return true;
		}
};

int main(){
	vector<vector<char> > board(9, vector<char>(9));
	
	for(int i=0; i<9; i++){
		for(int j=0; j<9; j++){
			cin >> board[i][j];
		}
	}
	
	Solution s;
	if(s.isValidSudoku(board)){
		cout << "true"; 
	}
	else{
		cout << "false";
	}
	
	return 0;
} 
