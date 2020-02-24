const array = [0,1,3,0,12];

function moveZeros(array){
  const maps = [];
  for(let i=0;i<=array.length-1;i++){
    if(array[i] === 0){
      maps.push(array[i]);
      array.splice(i,1);
    }
  }
  const last = array.concat(maps);
  console.log(last);
}

moveZeros(array);
