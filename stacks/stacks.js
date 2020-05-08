//stack linked list implementation
class Node{
    constructor(value){
      this.value = value;
      this.next = null;
    }
  }
  class Stack{
    constructor(){
      this.head = null;
      this.last = null;
      this.length = 0;
    }
  
    push(item){ //first in last out
      const newitem = new Node(item)
      if(this.length==0){
        this.head = newitem;
        this.last = newitem;
      }else{
        const current = this.head;
        this.head = newitem;
        this.head.next = current;
      }
      this.length++;
      return this;
    }
  
    pop(){
      if(this.length==0){
        console.log("this stack is empty")
        this.last = null;
      }else{
        //let current = this.head;
        this.head = this.head.next;
        this.length--;
        return this;
      }
    }
  }
  
  const mystack = new Stack();
  console.log(mystack.push("google"));
  console.log(mystack.push("twitter"));
  console.log(mystack.push("medium"));
  console.log(mystack.push("pocket"));
  console.log(mystack.pop());
  
//array implementation 
class Node{
    constructor(value){
      this.value = value;
    }
  
  }
  class Stack{
    constructor(){
      this.array = [];
    }
    push(newitem){
      this.array.push(newitem);
      return this;
    }
  
    pop(){
      if(this.array.length ==0){
        console.log("Stack has no item")
      }else{
        this.array.pop()
        return this;
      }
    }
  
  }
  
  const mystack = new Stack();
  console.log(mystack.push("google"));
  console.log(mystack.push("youtube"));
  console.log(mystack.push("twitter"));
  console.log(mystack.push(5));
  console.log(mystack.pop());