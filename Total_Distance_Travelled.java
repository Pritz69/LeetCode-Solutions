class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int rem=mainTank%5;
        int c=mainTank/5;
        int d=mainTank;
        while( c != 0)
        {
            if (additionalTank >=1)
            {
                additionalTank -=1;
                rem +=1;
                if (rem ==5)
                {
                    c +=1;
                    rem = 0;
                }
                                        /*
                                        if (rem >=5)
                                        {
                                            c +=1;
                                            rem = rem%5;
                                        }*/
                d +=1;
            }
            c -=1;
        }
        return d*10;
    }
}
/* class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int dist = 0;
        while(mainTank>0)
        {
            if(mainTank>=5)
            {
                mainTank-=5;
                dist +=50;
                if(additionalTank>0)
                {
                    additionalTank-=1;
                    mainTank+=1;
                }
            }
            else
            {
                dist = dist+((mainTank)*10);
                break;
            }
        }
        return dist;
    }
}
*/
