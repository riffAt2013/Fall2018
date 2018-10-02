//link: https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem

#include <bits/stdc++.h>
using namespace std;

string numarray[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

int main()
{
	
    int n; cin>>n;
    
    if (n>=1 && n<=9) cout<<numarray[n-1];
    else
        cout<<"Greater than 9";
}