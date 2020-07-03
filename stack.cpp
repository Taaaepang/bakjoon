#include <iostream>

using namespace std;

// stack 구현

class stack{
private:
    int st[1000];
    int size;
public:
    stack(){
        size = 1;
    }
    void push(int a)
    {
        if(size > 1000)
            cout << "stack is full \n";
        else
        {
            st[size+1] = a;
            size++;
        }
    }
    void pop()
    {
        if(size < 1)
            cout << "stack is empty \n";
        else
        {
            st[size-1] = 0;
            size--;
        }
    }
    int top()
    {
        if(size < 1){
            cout << "stack is empty \n";
            return -1;
        }
        else
            return st[size-1];
    }
};