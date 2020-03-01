// O(r*c) => r-row of matris, c-column of matris

function encryptString(str){
    str = str.replace(/\s+/g, '');
    strLen = str.length;
    sqrt = Math.sqrt(strLen);
    row = Math.floor(sqrt);
    column = Math.ceil(sqrt);
  
    if((row * column) < strLen){
      row = Math.ceil(sqrt)
    }
  
    let arr = [];
  
    for(let i=0;i<row;i++){
      let stringof = [];
      for(let j=0;j<column;j++){
        if((column*i)+j< strLen){
          stringof.push(str.charAt((column*i) + j))
        }
      }
      arr.push(stringof);
    }
  
    let newstr = "";
    for(let c=0;c<column;c++){
      //newstr = newstr + " ";
      for(let r=0;r<row;r++){
        if(c<arr[r].length){
          newstr = newstr + arr[r][c];
        } 
  
      }
      newstr = newstr + " ";
    }
  
    console.log(arr);
    console.log(newstr);
  
  }
  encryptString("this is a rest")