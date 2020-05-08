const myarr = [1,2,3,1,3];
function findDuplicate(myarr){
  const hTable = {};
  for(let i = 0; i < arr.length; i++){
    let index = myarr[i]
    // Bu if saglanirsa duplicated vardir zaten.
    if(index in hTable)
    {
      hTable[index] = hTable[index]+1;
    }
    else{
      hTable[myarr[i]] = 1;
    }
  }

  console.log(hTable)
}
findDuplicate(arr)

const arr = [2,5,1,2,3,5,1,2,4];
//Given an array finds all recurrings
function findRecurrings(arr){
  let htable = {};
  for (let i=0; i<arr.length; i++){
    if(!(htable[arr[i]])){
      htable[arr[i]] = 1
    }else{
      htable[arr[i]] = htable[arr[i]] + 1
    }
  }
    console.log(htable)
  for(let i=0;i<arr.length;i++){
    if(htable[i] > 1){
      console.log("Recurring character",i)
    }
  }
}

findRecurrings(arr);

//Finds first recurring
function firstRecuringItem(arr){
  let mytable = {};
  for (let i=0; i<arr.length; i++){
    if(arr[i] in mytable){
      return arr[i]    
      }else {
      mytable[arr[i]] = true
    }
  }
  return undefined;
}
firstRecuringItem(arr)
//It should return 2
