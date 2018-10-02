//link: https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem
#include <bits/stdc++.h>
using namespace std;

bool even (int n) {
	return (n%2==0);
}

string numarray[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

int main ()
{
	int first, second;
	cin>>first; cin>>second;
	for (int a= first; a<=second; a++)
	{
    	if (a>=1 && a<=9) 
    		{
    			cout<<numarray[a-1]<<'\n';
    			continue;
    		}
		if	(even(a) == true) cout<< "even"<<'\n';
		else cout<< "odd"<<'\n';
	}
	return 0;
}