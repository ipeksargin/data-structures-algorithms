const arr = [1,2,3,1,3];
function findDuplicate(arr){
  const hTable = {};
  for(let i = 0; i < arr.length; i++){
    let index = arr[i]
    // Bu if saglanirsa duplicated vardir zaten.
    if(index in hTable)
    {
      hTable[index] = hTable[index]+1;
    }
    else{
      hTable[arr[i]] = 1;
    }
  }

  console.log(hTable)
}

findDuplicate(arr)
