int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize){
    int ans=0 , i , a , b ;
    for(i=0;i<pointsSize-1;i++){
        a=points[i+1][0]-points[i][0];
        if(a<0){
            a = a*-1;
        }
        b=points[i+1][1]-points[i][1];
        if(b<0){
            b = b*-1;
        }
        if(a>b){
            ans=ans+a;
        } else {
            ans=ans+b;
        }
    }
    return ans;

}
