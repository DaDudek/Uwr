$("img").click(function (){
    if ($(this).data("marked") === "true"){
        unmark($(this));
    }
    else {
        mark($(this))
    }
});

function markAll(){
    $("img").each(function (){
        mark($(this));
    })
}

function unmarkAll(){
    $("img").each(function (){
        unmark($(this));
    })
}

function mark(image){
    image.css({"border-width": "3px", "border-style": "solid", "border-color": "red"});
    image.data("marked", "true");
}

function unmark(image){
    image.css({"border-width": "0px", "border-style": "none", "border-color": "white"});
    image.data("marked", "false");
}

function writeAll(){
    let text = ""
    $("img").each(function (){
        if ($(this).data("marked") === "true"){
            text = text + $(this).attr('id') +" ";
        }
    })
    $("#value").val(text);
}

$("#markAllBt").on("click", markAll);
$("#unmarkAllBt").on("click", unmarkAll);
$("#writeAllBt").on("click", writeAll);
