let timer = 0;
let t = 0
let startValue= '200px'
let endValue = '400px'
let flag = true
let div = document.getElementById('container');
let divs = div.getElementsByTagName('div');

function myFunction(){

    if(flag === true) {
        if (divs[t].style.marginTop >= endValue) {
            t = t + 1;
        }
        if(t === 4) {
            t = 0;
            flag = flag !== true;
        }
        myFunctionDownOneElem(t);
    }
    else {
        if (divs[t].style.marginTop <= startValue) {
            t = t + 1;
        }
        if(t === 4) {
            t = 0;
            flag = flag !== true;
        }
        myFunctionUpOneElem(t);
    }

    timer = setTimeout("myFunction()", 20);

}


function myFunctionDownOneElem(i) {

    if (divs[i].style.marginTop === ""){
        divs[i].style.marginTop = startValue;
    }
    else {
        let x = (parseInt(divs[i].style.marginTop.replace(/px/,"")))
        let y = x + 5;
        divs[i].style.marginTop = y + "px";
        }

}



function myFunctionUpOneElem(i) {
    if (divs[i].style.marginTop === ""){
        divs[i].style.marginTop = endValue;
    }
    else {
        let x = (parseInt(divs[i].style.marginTop.replace(/px/,"")))
        let y = x - 5;
        divs[i].style.marginTop = y + "px";
    }
}