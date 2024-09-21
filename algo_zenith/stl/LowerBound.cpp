#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main()
{
    vector<int> arr = {10, 20, 30, 40, 50};
    auto lower_index = lower_bound(arr.begin(), arr.end(), 35);
    if (lower_index != arr.end())
    {
        cout << "Lower index is " << lower_index - arr.begin() << "\n";
        cout << "Value of lower index is " << *lower_index << "\n";
    }
    else
    {
        cout << "Lower bound is not available" << "\n";
    }
    auto upper_index = upper_bound(arr.begin(), arr.end(), 35);
    if (upper_index != arr.end())
    {
        cout << "Upper index is " << upper_index - arr.begin() << "\n";
        cout << "Upper index value is " << *upper_index << "\n";
    }
    else
    {
        cout << "Upper Bound not available" << "\n";
    }
    vector<int> v = {10, 20, 30, 30, 40, 50};

    // Lower bound for 30
    auto lb = lower_bound(v.begin(), v.end(), 30);

    // Upper bound for 30
    auto ub = upper_bound(v.begin(), v.end(), 30);

    cout << "Lower bound of 30 is at index: " << lb - v.begin() << " (Value: " << *lb << ")" << endl;
    cout << "Upper bound of 30 is at index: " << ub - v.begin() << " (Value: " << *ub << ")" << endl;

    return 0;
}

/*
#include<bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {10, 20, 30, 40, 50};

    // Find the first element that is not less than 35
    auto it = lower_bound(v.begin(), v.end(), 35);

    if (it != v.end()) {
        cout << "Lower bound of 35 is at index: " << it - v.begin() << endl;
        cout << "Value: " << *it << endl;
    } else {
        cout << "35 is greater than all elements." << endl;
    }

    return 0;
}
*/