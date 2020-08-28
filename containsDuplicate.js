var containsDuplicate = function(nums) {
    let ob = {}
    let arr = false
    nums.forEach(i => {
        if(!ob[i]){
            ob[i]=0
        }
        ob[i] += 1
    })
    for(let i in ob){
        if(ob[i] >= 2){
            arr =  true
        } 
    }
    return arr
    
};