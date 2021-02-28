const input = $("#searchphrase");

function check(){
    let submitValue = input.val();
    clear();
    if (submitValue.length >= 3) {
        $("#items").find("li").each(function (i) {
            if ($(this).text().includes(submitValue)) {
                let text = $(this).text();
                $(this).html(text.replace(submitValue, "<span class='found'>" + submitValue + "</span>"));
            } else {
                $(this).css("color", "gray");
            }
        })
    }
};

function clear(){
    $("#items").find("li").each(function (i) {
        let text = $(this).text();
        $(this).html(text.replace("<span class='found'>", ""));
        $(this).html(text.replace("</span>", ""));
        $(this).css("color", "black")
    })
}



input.on("input",check);


