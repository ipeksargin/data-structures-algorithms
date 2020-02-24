
const array=[2,7,11,15];

function twoSum(array, target) {
    let list = {};
    for(let i=0;i<=array.length-1;i++){
      let item = target - array[i];
      if(!list[item]){
        list[item] = true
      }
      if(array[i] in list){
        console.log("founded", array[i], "plus",target-array[i])
      }
    }

};
twoSum(array,9);
