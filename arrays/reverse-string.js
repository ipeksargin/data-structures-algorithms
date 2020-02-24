//Long way O(n)

function reverse(str){
  let contain = [];
  let strLong = str.length - 1;
  for(let i=strLong;i>=0;i--){
    contain.push(str[i]);
  }
  return contain;
}
reverse('hellohello')

//Short way

function reverse2(str){
  return str.split('').reverse().join('');
}
reverse2('hello')
