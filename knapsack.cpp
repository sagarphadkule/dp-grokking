using namespace std;

#include <iostream>
#include <vector>


// WITHOUT space optimization
class Knapsack {
public:
  int solveKnapsack(const vector<int> &profits, const vector<int> &weights, int capacity) {
    //TODO: Write - Your - Code
    int nitems = profits.size();

    if (nitems == 0 || capacity == 0) {
        return 0;
    }

    // Table indicates Total Profit if only upto i'th items are available, and only c capacity is remaining.
    vector<vector<int>> totalProfits(nitems, vector<int>(capacity+1, 0));

    // For capacitiy 0, we can take 0 items so 0 total profit:
    for (int i = 0; i < nitems; i++) {
        totalProfits[i][0] = 0;
    }

    // If we could only take the 1st item, then totalProfit = profits[0]... provided we can take that item.
    for (int c = 0; c <= capacity; c++) {
        if (weights[0] <= c) {
            totalProfits[0][c] = profits[0];
        } // else 0.        
    }

    for (int i = 1; i < nitems; i++) {
        for (int c = 1; c <= capacity; c++) {
            
            // If we can take this item:
            int profit1 = 0;
            if (weights[i] <= c) {                
                // Profit of this item + whatever is the max profit achievable for the remaining capacity & remaining items before this item.
                profit1 = profits[i] + totalProfits[i-1][c - weights[i]];
            }
            
            //else if this item exceeds capacity, then we'll have to fallback on upto previous items for max achievable totalprofit.
            int profit2 = totalProfits[i-1][c];

            // So the totalProfit achievable is the max of either of the above two cases.
            totalProfits[i][c] = max(profit1, profit2);
        }
    }

    return totalProfits[nitems-1][capacity];
  }
};


// space optimization 1
class Knapsack {
public:
  int solveKnapsack(const vector<int> &profits, const vector<int> &weights, int capacity) {
    //TODO: Write - Your - Code
    int nitems = profits.size();

    if (nitems == 0 || capacity == 0) {
        return 0;
    }

    // Table indicates Total Profit if only upto i'th items are available, and only c capacity is remaining.
    // But we dont need to maintain all rows,.. just upto the "previous" item's row and current row.
    vector<vector<int>> totalProfits(2, vector<int>(capacity+1, 0));

    // For capacitiy 0, we can take 0 items so 0 total profit:
    for (int i = 0; i < 2; i++) {   // loop only for 2 rows.
        totalProfits[i][0] = 0;
    }

    // If we could only take the 1st item, then totalProfit = profits[0]... provided we can take that item.
    for (int c = 0; c <= capacity; c++) {
        if (weights[0] <= c) {
            totalProfits[0][c] = profits[0];
        } // else 0.        
    }

    for (int i = 1; i < nitems; i++) {
        for (int c = 1; c <= capacity; c++) {
            int prevI = (i-1) % 2;  // Since we'll maintain only two rows of items.
            int currI = i % 2;
            // If we can take this item:
            int profit1 = 0;
            if (weights[currI] <= c) {                
                // Profit of this item + whatever is the max profit achievable for the remaining capacity & remaining items before this item.                
                profit1 = profits[currI] + totalProfits[prevI][c - weights[currI]];
            }
            
            //else if this item exceeds capacity, then we'll have to fallback on upto previous items for max achievable totalprofit.
            int profit2 = totalProfits[prevI][c];

            // So the totalProfit achievable is the max of either of the above two cases.
            totalProfits[currI][c] = max(profit1, profit2);
        }
    }

    return totalProfits[1][capacity];
  }
};


// SPACE Optimization 2:

class Knapsack {
public:
  int solveKnapsack(const vector<int> &profits, const vector<int> &weights, int capacity) {
    //TODO: Write - Your - Code
    int nitems = profits.size();

    if (nitems == 0 || capacity == 0) {
        return 0;
    }

    // Table indicates Total Profit for each capacity. We will update these values as we iterate over all items.
    vector<int> totalProfits(capacity+1, 0);

    // If we can take the first item, then thats the profit:
    for (int c = 0; c <= capacity; c++) {
        if (weights[0] <= c) {
            totalProfits[c] = profits[0];
        } // else 0.        
    }

    for (int i = 1; i < nitems; i++) {
        for (int c = 1; c <= capacity; c++) {
            // If we can take this item:
            int profit1 = 0, profit2 = 0;

            if (weights[i] <= c) {                
                // Profit of this item + whatever is the max profit achievable for the remaining capacity & remaining items before this item.                
                profit1 = profits[i] + totalProfits[c - weights[i]];
            }
            
            //else if this item exceeds capacity, then we'll have to fallback on upto previous items' max achievable totalprofit.
            int profit2 = totalProfits[c];

            // So the totalProfit achievable is the max of either of the above two cases.
            totalProfits[c] = max(profit1, profit2);
        }
    }

    return totalProfits[capacity];
  }
};
