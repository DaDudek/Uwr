const table = $("#searchData");
const button = $("#send");
const input = $("#searchphrase");
function clear(){
    table.html("");
}



$(document).ready(function() {
    $.get("https://tvn24.pl/najnowsze.xml", function(data) {
        let xmlDocument = data;
        let counter=0;
        $(xmlDocument).find( "item" ).each(function () {
            if(counter===5) {
                return false;
            }
            addToTable($("#data"), "<a href='" + $(this).find("link").text() + "'>",$(this).find("title").text(),$(this).find("description").text());
            counter++;
        })
        ;
    })

    function addToTable(table,source,title,description){
        table.append(
            "<tr><td>"+ source + "source</a></td>" +
            "<td>" + title + "</td>" +
            "<td>" + description + "</td></tr>");
    }

    function search(){
        $.get("https://tvn24.pl/najnowsze.xml", function(datas) {
            clear();
            table.append("<tr>" +
                "<th>Source</th>" +
                "<th>Title</th>" +
                "<th>Description</th>" +
                "</tr>")
            for (const element of $(datas).xpath("/rss/channel/item")){
                let description = $(element).xpath("./description/text()")[1].data;
                console.log(description);
                if (description.includes(input.val()))
                {
                    let source = '<a href="' + ($(element).xpath("./link/text()")[0].data) + '">';
                    let title = ($(element).xpath("./title/text()")[0].data);
                    addToTable(table,source,title,description);
                }

            }
    })
    }

    button.on("click",search);
});

