//https://www.hackerrank.com/challenges/birthday-cake-candles/problem

#include <iostream>         
#include <algorithm>

using namespace std;

int main ()
{
    int n; cin>>n;
    int arr[n];
    
    for (int i=0; i<n; i++)
        cin>>arr[i];
    sort (arr, arr+n, greater<int>());
    int max = arr[0];
    int count = 0;
    for (int i: arr)
        if (i == max) count++;
    cout<<count;
}
		
