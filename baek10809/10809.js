const input = "baekjoon";
let data = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1];
for(i=0; i<input.length; i++){
    asci = input.charCodeAt(i)-97;
    data[asci]=i;
};
for(i=0; i<data.length; i++){
    console.log(data[i])
}

///맞는데 백준에서는 왜 런타임에러가 나는지 모르겠음