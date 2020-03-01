let magazineStr = 'give me one grand night';
let messageStr = 'give one grand today';

const compareMessages = (magazineStr, messageStr)=>{

    let messageArr = messageStr.split(' ');
    let magazineArr = magazineStr.split(' ');

    let table = {}

    magazineArr.forEach(element => {
        table[element] = 1; 
    });

    for(let i=0;i<messageArr.length;i++)
    {
        if(!(messageArr[i] in table))
        {
            return "NO";
        }
    }

    return "YES";
}

console.log(compareMessages(magazineStr,messageStr));