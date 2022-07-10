#define min(X, Y) ((X) < (Y) ? (X) : (Y))

int minCostClimbingStairs(int* cost, int costSize){
    
    //Dynamic programming
    if (costSize == 2) return min(cost[0], cost[1]);
    
    int pay[costSize];
    pay[0] = cost[0];
    pay[1] = cost[1];
    
    for(int i=2; i<costSize; i++){
        pay[i] = min(pay[i-1], pay[i-2]) + cost[i];   //minimum cost to reach index i
    }
    return min(pay[costSize-1], pay[costSize-2]);

}
