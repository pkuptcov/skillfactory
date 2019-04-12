function get_forecasts() {
    $.getJSON('https://sf-pyw.mosyag.in/m04/api/forecasts', function(data) {paragraphs = data["prophecies"]})
}

function set_content_in_divs() {
    get_forecasts()
    $.each(paragraphs, function(i, d) {
        p = $("#p-" + i);
        p.html("<p>" + d + "</p>");
    })
}