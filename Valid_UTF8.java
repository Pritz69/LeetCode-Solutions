class Solution {
public boolean validUtf8(int[] data) {
        int remBytes = 0;
        for(int var : data) 
        {
            if(remBytes == 0) 
            {
                if((var >> 7) == 0b0)
                { // 1byte
                    remBytes = 0;
                } 
                else if((var >> 5) == 0b110) 
                { // 2 byte
                    remBytes = 1;
                }  
                else if ((var >> 4) == 0b1110) 
                { // 3 byte
                    remBytes = 2;
                }
                else if((var >> 3) == 0b11110) 
                { // 4byete
                    remBytes = 3;
                } 
                else
                {
                    return false;
                }
            } 
            else 
            {
                if((var >> 6) == 0b10)
                {
                    remBytes--;
                } 
                else 
                {
                    return false;
                }
            }
        }
        
        if(remBytes == 0)
        {
            return true;
        }
        else 
        {
            return false;
        }
    }
}
