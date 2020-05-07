arr1 =[0,3,4,31];
arr2=[2,4,6,30]

function mergeSortedArrays(arr1, arr2){
  const final = [];
  arr1Item = arr1[0];
  arr2Item = arr2[0];
  let i = 1;
  let j =1;

  if(arr1.length == 0){
    return arr2;
  }
  if(arr2.length == 0){
    return arr1;
  }
  while(arr1Item || arr2Item){
    if(!arr2Item || arr1Item<arr2Item){
      final.push(arr1Item);
      arr1Item = arr1[i];
      i++;
    }
    else{
      final.push(arr2Item);
      arr2Item = arr2[j];
      j++;
    }
    
  }
  console.log(final);
}
mergeSortedArrays(arr1,arr2)