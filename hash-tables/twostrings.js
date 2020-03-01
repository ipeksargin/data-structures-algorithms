let str1 = "cat";
let str2 = "a";

function twoStrings(str1, str2){
    let table = {};

    for(let i=0;i<str1.length;i++){
        table[str1.charAt(i)] = 1;
    }
    console.log(table);
    for(let i=0;i<str2.length;i++){
        if(str2.charAt(i) in table)[
        console.log(str2[i])
        ]
    }
}

twoStrings(str1, str2);