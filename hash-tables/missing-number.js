function missingValue(array1, array2){
    let map1 = {};
    for(let i = 0; i<=array1.length-1;i++){
      if(!map1[array1[i]]){
        map1[array1[i]] = 1;
      }
      else{
        map1[array1[i]] =  map1[array1[i]] + 1;
      }
    }
    let map2 = {};
    for(let x = 0; x<=array2.length-1;x++){
      if(!map2[array2[x]]){
        map2[array2[x]] = 1;
      }else{
        map2[array2[x]] = map2[array2[x]] + 1;
      }
    }
    const keys1 = Object.keys(map1);
    const arr = [];
    for(let a = 0; a<=keys1.length-1;a++){
      if(!map2[keys1[a]] || (map2[keys1[a]] && map2[keys1[a]]!=map1[keys1[a]])){
        arr.push(parseInt(keys1[a]));
      }
    }
    console.log(map1);
    console.log(map2);
    console.log(keys1);
    console.log(arr);
  
  
  }
  
  const one = [1,2,3,4,5,6,7,7,7,1];
  const two = [4,5,6,7,8,2];
  missingValue(one,two);
  