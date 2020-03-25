array1 = [4,9,5];
array2 = [4,9,8,4];

function insersectArr(array1,array2){
  let map={}
  for(let i=0; i<array1.length;i++){
    if(!map[array1[i]]){
      map[array1[i]] = 1
    }else{
      map[array1[i]] = map[array1[i]] + 1;
    }
  }
  //console.log(map)

  for(let k=0;k<array2.length;k++){
    if(!map[array2[k]]){
      map[array2[k]] = 1
    }else{
      map[array2[k]] = map[array2[k]] + 1;
    }
  }
 // console.log(map)
  let final = [];
  const mapkeys = Object.keys(map); 
  // way to reach hash table key so that I can reach values
  //console.log(mapkeys);
  for(let x=0;x<mapkeys.length;x++){
   if(map[mapkeys[x]] > 1){
     final.push(mapkeys[x])
   }
  }
  console.log(final)
}
insersectArr(array1,array2)