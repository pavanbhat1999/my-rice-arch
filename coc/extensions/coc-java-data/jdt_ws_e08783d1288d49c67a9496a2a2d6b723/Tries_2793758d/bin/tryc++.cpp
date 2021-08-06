#include<iostream>
#include <ostream>
#include <stdio.h>
using namespace std;
int add(int a,int b){
    int c=0;
    c = a+b;
    //c=newbranchi request;
    return c;
}
int main()
{
    cout<<"Hello World\n";
    cout<<add(2,3)<<endl;
    return 0;
}
