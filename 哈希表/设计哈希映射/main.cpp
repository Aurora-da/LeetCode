#include<iostream>
#include<vector>
using namespace std;

class MyHashMap{
private:
	// 定义链表节点
	struct Node{
		int key;
		int value;
		Node* next;
		Node(int k, int v) : key(k), value(v), next(nullptr){}
	}; 
	
	// 哈希表的大小
	static const int SIZE = 1007;
	vector<Node*> buckets;
	
	// 哈希函数
	int hash(int key){
		return key % SIZE;
	} 
	
public:
	MyHashMap(){
		buckets.resize(SIZE, nullptr);
	}
	
	void put(int key, int value){
		int index = hash(key);
		Node* head = buckets[index];
		
		if(head == nullptr){
			buckets[index] = new Node(key, value);
			return;
		}
		
		Node* curr = head;
		Node* prev = nullptr;
		// 寻找这个键是否已经存在，如果存在的话则就更新这个键所对应的值 
		while(curr != nullptr){
			if(curr->key == key){
				curr->value = value;
				return;
			}
			prev = curr;
			curr = curr->next;
		}
		
		// 没有在链表中找到这个键 
		prev->next = new Node(key, value);
	}
	
	int get(int key){
		int index = hash(key);
		Node* curr = buckets[index];
		
		while(curr != nullptr){
			if(curr->key == key){
				return curr->value;
			}
			curr = curr-> next;
		} 
		
		return -1;
	}
	
	void remove(int key){
		int index = hash(key);
		Node* curr = buckets[index];
		Node* prev = nullptr;
		
		while(curr != nullptr){
			if(curr->key==key){
				if(prev==nullptr){
					buckets[index] = curr->next;
				}
				else{
					prev->next=curr->next;
				}
				delete curr;
				return;
			}
			prev = curr;
			curr = curr->next;
		}
	}
};

int main(){
	
	
	
	
	
	return 0;
} 
