const one = [1,2,3,4,5,6,7,7,7,1];
const two = [4,5,6,7,8,2];

function missingValue(array1, array2){
let table = {};
// filling hash table with array1 items
for(let i=0; i<=array1.length-1;i++){
    if(!table[array1[i]]){
        table[array1[i]] = 1;
    }else{
        table[array1[i]] = table[array1[i]] + 1;
    }
}
for(let i=0; i<=array2.length-1;i++){
    if(table[array2[i]]){
        table[array2[i]] = table[array2[i]] -1;
    }
}
const tableKeys = Object.keys(table);
const arr = [];
for(let i=0; i<=tableKeys.length-1;i++){
    if(table[tableKeys[i]]>0){
        arr.push(tableKeys[i]);
        console.log(arr);
    }
}

}
missingValue(one,two);