const arrOne = ["one", 11, "two", 3, "four", 5];
const arrTwo = ["six", 7, "eight", "nine", 9,11];

//Short way
function findCommon(arr1, arr2){
return arr1.some(item => arr2.includes(item))
}
findCommon(arrOne,arrTwo)

//Long way
function finditem(arr1,arr2){
  let list={};
  for(let i=0;i<=arr1.length-1;i++){
    if(!list[arr1[i]]){
      list[arr1[i]] = true;
    }
  }
  //console.log(list);
  for(let j=0;j<=arr2.length-1;j++){
    if(list[arr2[j]]){
      console.log("same item found");
      console.log(arr2[j]);
    }
  }
}
finditem(arrOne,arrTwo)
