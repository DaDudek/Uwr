window.onload = load;

function load()
{
    addMarkaOnStart("Honda");
    addMarkaOnStart("Kia");
    addModelOnStart("Honda", "Civic");
    addModelOnStart("Honda", "Jazz");
    addModelOnStart("Kia", "Ceed");
    addModelOnStart("Kia", "Stinger");
    giveSelection(sel1.value);
}

function addMarkaOnStart(nazwa)
{
    var selectMenu = document.getElementById("marka");
    var optionToAdd = document.createElement("option");
    optionToAdd.appendChild( document.createTextNode(nazwa));
    optionToAdd.value = nazwa; 
    selectMenu.appendChild(optionToAdd);
}

function addModelOnStart(markaNazwa, modelNazwa)
{
    var selectMenu = document.getElementById("model");

    var optionToAdd = document.createElement("option");

    optionToAdd.appendChild( document.createTextNode(modelNazwa));
    var str = "value";
    optionToAdd.setAttribute(str, markaNazwa);
    selectMenu.appendChild(optionToAdd);
    var newElems = selectMenu.querySelectorAll('option');
    var elems = Array.prototype.slice.call(newElems);
    list.push.apply(list, elems);
}


function markaRadioCheckChange()
{
    document.getElementById("modelRadio").checked = false;
}

function modelRadioCheckChange()
{
    document.getElementById("markaRadio").checked = false;
}


function addElem()
{

    var modelRadioCheck = document.getElementById("modelRadio").checked;
    var markaRadioCheck = document.getElementById("markaRadio").checked;

    if(markaRadioCheck == true)
    {
        var selectMenu = document.getElementById("marka");
        var selectMenuValue = selectMenu.value;

        var optionToAdd = document.createElement("option");
        var optionTextToAdd = document.getElementById("nowa").value;

        optionToAdd.appendChild( document.createTextNode(optionTextToAdd));
        optionToAdd.value = optionTextToAdd; 
        selectMenu.appendChild(optionToAdd);
    } else
    {
        var selectMenu = document.getElementById("model");

        var markaValue = document.getElementById("marka").value;

        var optionToAdd = document.createElement("option");
        var optionTextToAdd = document.getElementById("nowa").value;

        optionToAdd.appendChild( document.createTextNode(optionTextToAdd));
        var str = "value";
        optionToAdd.setAttribute(str, markaValue);
        selectMenu.appendChild(optionToAdd);
        var newElems = selectMenu.querySelectorAll('option');
        var elems = Array.prototype.slice.call(newElems);
        list.push.apply(list, elems);
    }

}


var sel1 = document.querySelector('#marka');
var sel = document.getElementsByName("marka");
var sel2 = document.querySelector('#model');
var options2 = sel2.querySelectorAll('option');
var list = Array.prototype.slice.call(options2);

function giveSelection(selValue) {
    sel2.innerHTML = '';
    for(var i = 0; i < list.length; i++) {
        if(list[i].value === selValue) {
            console.log(list[i]);
        sel2.appendChild(list[i]);
        }
    }
}

giveSelection(sel1.value);




