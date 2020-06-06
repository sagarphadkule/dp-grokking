using namespace std;

#include <iostream>
#include <vector>

// MINE:
#include <algorithm>
class PartitionSet {
public:
    int canPartition(const vector<int> &nums) {
        using namespace std;

        int Sum = accumulate(nums.begin(), nums.end(), 0);
        int halfSum = Sum/2;

        // We want to create a subset whose sum is as close as possible to halfSum.
        // eg. {1,2,3,4}

        // n/s 0   1   2   3
        // 1   0   1   1   1
        // 2   0   1   2   3
        // 3   0   1   2   3
        // 4   0   1   2   3


        int n = nums.size();
        vector<vector<int>> closestSum(n, vector<int>(halfSum+2, -1));

        for (int i = 0; i < n; i++) {
            closestSum[i][0] = 0;
        }

        for (int s = 0; s <= halfSum+1; s++) {
            closestSum[0][s] = (nums[0] <= s) ? nums[0] : 0;
        }

        for (int i = 1; i < n; i++) {
            int currNum = nums[i];
            for (int s = 1; s <= halfSum+1; s++) {

                int closestIfInclude = -1, closestIfExclude = -1;

                if (nums[i] <= s) {               
                    closestIfInclude = nums[i] + closestSum[i-1][s - nums[i]];
                }
                
                closestIfExclude = closestSum[i-1][s];
                closestSum[i][s] = max(closestIfInclude, closestIfExclude);
            }
        }

        int minDiff;
        if (Sum % 2 == 0) {
            int set1sum = closestSum[n-1][Sum/2];
            int set2sum = Sum - set1sum;
            minDiff = abs(set1sum - set2sum);
        }
        else  {
            int set1sum = closestSum[n-1][Sum/2];
            int set2sum = Sum - set1sum;
            int minDiff1 = abs(set1sum - set2sum);;
            
            int set1sum2 = closestSum[n-1][Sum/2+1];
            int set2sum2 = Sum - set1sum2;
            int minDiff2 = abs(set1sum2 - set2sum2);
            minDiff1 = min(minDiff1, minDiff2);
        }

        return minDiff;
    }
};



// // THEIRS:
// class PartitionSet {
// public:
//   int canPartition(const vector<int> &num) {
//     int sum = 0;
//     for (int i = 0; i < num.size(); i++) {
//       sum += num[i];
//     }

//     int n = num.size();
//     vector<vector<bool>> dp(n, vector<bool>(sum / 2 + 1, false));

//     // populate the sum=0 columns, as we can always form '0' sum with an empty set
//     for (int i = 0; i < n; i++) {
//       dp[i][0] = true;
//     }

//     // with only one number, we can form a subset only when the sum is equal to that number
//     for (int s = 0; s <= sum / 2; s++) {
//       dp[0][s] = (num[0] == s ? true : false);
//     }

//     // process all subsets for all sums
//     for (int i = 1; i < num.size(); i++) {
//       for (int s = 1; s <= sum / 2; s++) {
//         // if we can get the sum 's' without the number at index 'i'
//         if (dp[i - 1][s]) {
//           dp[i][s] = dp[i - 1][s];
//         } else if (s >= num[i]) {
//           // else include the number and see if we can find a subset to get the remaining sum
//           dp[i][s] = dp[i - 1][s - num[i]];
//         }
//       }
//     }

//     int sum1 = 0;
//     // Find the largest index in the last row which is true
//     for (int i = sum / 2; i >= 0; i--) {
//       if (dp[n - 1][i] == true) {
//         sum1 = i;
//         break;
//       }
//     }

//     int sum2 = sum - sum1;
//     return abs(sum2 - sum1);
//   }
// };

int main(int argc, char *argv[]) {
  PartitionSet ps;
  vector<int> num = {1, 2, 3, 9};
  cout << ps.canPartition(num) << endl;
  num = vector<int>{1, 2, 7, 1, 5};
  cout << ps.canPartition(num) << endl;
  num = vector<int>{1, 3, 100, 4};
  cout << ps.canPartition(num) << endl;
}