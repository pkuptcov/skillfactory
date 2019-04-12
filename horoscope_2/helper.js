function getData() {
    $.getJSON('https://sf-pyw.mosyag.in/m04/api/forecasts', function(data) {paragraphs = data["prophecies"]})
}

function set_content_in_divs() {
    getData()
    $.each(paragraphs, function(i, d) {
        p = $("#p-" + i);
        p.html("<p>" + d + "</p>");
    })
}