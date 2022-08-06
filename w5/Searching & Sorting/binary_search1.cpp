
/*  
Author: Syed Faysel Ahammad Rajo
handle: syedrajo20
*/

#include<bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);


    int arr[] = {2,3,5,6,7,8,9};
    int l=0, r=7;
    // int mid = l+ (r-l)/2;
    int target; cin>>target;
    while(l<=r)
    {
        int mid = l+ (r-l)/2;
        if (arr[mid] == target)
        {
            cout<<mid<<endl;
            break;
        }
        else if(arr[mid]<target){
            l = mid+1;
        }
        else if (arr[mid]>target){
            r = mid - 1;
        }
        else{
            cout<<"Not found";
        }
    }



    return 0;
}