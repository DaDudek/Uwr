const adjectives = ["Głodny", "Brzydki", "Niechlubny", "Straszliwy", "Zabawny", "Elegancki", "Smutny", "Miły", "Czerwony","Denerwujący"];
const nouns = ["agent nieruchomości", "artysta", "bankowiec", "biotechnolog", "dekarz", "fryzjer", "informatyk", "kontroler ruchu lotniczego", "lekarz", "złodziej"];
const verbs = ["absorbuje", "batoży", "alkalizuje", "bije", "ciska","cedzi","zjada", "maluje", "drwi", "zabawia"];
const rests = ["niezdrowo", "podczas przerwy na lunch", "w czasie poloneza", "na słonecznej polanie", "w samej bieliznie", "z piękną kochanką", "trzymając czerwony parasol", "podczas zawodów w gry na pianinie","podczas rejsu kajakiem po odrze","a jego brat okrada swoich sąsiadów"];


function init(){
   initAdjectives();
   initNouns();
   initVerbs();
   initRests();
}

function initAdjectives(){
let List = $("ul[data-type='adjectives']");
$.each(adjectives, function(i)
{
    let li = $('<li/>')
        .addClass('ui-menu-item')
        .attr('role', 'menuitem')
        .appendTo(List);
    let text = $('<p/>')
        .text(adjectives[i])
        .appendTo(li);
});
}

function initNouns(){

    let List = $("ul[data-type='nouns']");
    $.each(nouns, function(i)
    {
        let li = $('<li/>')
            .addClass('ui-menu-item')
            .attr('role', 'menuitem')
            .appendTo(List);
        let text = $('<p/>')
            .text(nouns[i])
            .appendTo(li);
    });
}

function initVerbs(){

    let List = $("ul[data-type='verbs']");
    $.each(verbs, function(i)
    {
        let li = $('<li/>')
            .addClass('ui-menu-item')
            .attr('role', 'menuitem')
            .appendTo(List);
        let text = $('<p/>')
            .text(verbs[i])
            .appendTo(li);
    });
}

function initRests(){

    let List = $("ul[data-type='rests']");
    $.each(rests, function(i)
    {
        let li = $('<li/>')
            .addClass('ui-menu-item')
            .attr('role', 'menuitem')
            .appendTo(List);
        let text = $('<p/>')
            .text(rests[i])
            .appendTo(li);
    });
}

function generate(){
    let text = adjectives[Math.floor(Math.random() * adjectives.length)] + " "
            + nouns[Math.floor(Math.random() * nouns.length)] + " "
            + verbs[Math.floor(Math.random() * verbs.length)] + " "
            +rests[Math.floor(Math.random() * rests.length)];
    $("#value").val(text);
}
