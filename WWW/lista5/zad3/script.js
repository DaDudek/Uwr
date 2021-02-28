$(document).ready(function() {
    $.getJSON('tvn.json', {}, function (data) {
        console.log(data);
        for (let i = 0; i < 5; i++) {
            let source = "<a href='"+ Mustache.render(`{{rss.channel.item.${i}.link}}`,data) + "'>" ;
            let title = Mustache.render(`{{rss.channel.item.${i}.title.__cdata}}`,data);
            let description = Mustache.render(`{{rss.channel.item.${i}.description.__cdata}}`,data);
            addToTable($("#data"), source, title, description);
        }
    });

    function addToTable(table,source,title,description){
        table.append(
            "<tr><td>"+ source + "source</a></td>" +
            "<td>" + title + "</td>" +
            "<td>" + description + "</td></tr>");
    }
});