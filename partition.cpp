using namespace std;

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class PartitionSet {
public:
  bool canPartition(const vector<int> &nums) {
    //TODO: Write - Your - Code
    int Sum = accumulate(nums.begin(), nums.end(), 0);
    if (Sum % 2 == 1) {
        return false;
    }

    int sum = Sum/2;

    // i|0|1|2|..|s
    // ---
    // 1|f
    // 2|f t       
    // 3|        |t
    // 4|
    // 5|

    vector<bool> possibleSums(sum+1, false);

    for (int s = sum; s >= 0; s--) {
        possibleSums[s] = (nums[0] == s);
    }

    int n = nums.size();
    for (int i = 1; i < n; i++) {
        int currNum = nums[i];
        for (int s = sum; s >= 0; s--) {

            // If we exclude currNum:
            bool possible1 = possibleSums[s];
            
            // If we include currNum:
            bool possible2;
            if (currNum <= s) {
                possible2 = possibleSums[s-currNum];
            }            
            possibleSums[s] = possible1 || possible2;

            if (s == sum && possibleSums[s] == true) {
                break;
            }
        }
    }
        
    return possibleSums[sum];
  }


};

