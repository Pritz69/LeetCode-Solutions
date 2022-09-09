        properties.sort(key=lambda x: (-x[0],x[1]))
        ans=mx=0
        for a,d in properties :
            if d < mx :
                ans +=1
            mx=max(mx,d)
        return ans
