<html><head>
  <meta charset='utf-8'>
  <title>Гороскоп на сегодня</title>
  <link
    rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
    crossorigin="anonymous"
  />
  <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>

  <script language="javascript">
      function set_content_in_divs() {
          $.getJSON('http://sf-pyw.mosyag.in/m04/api/forecasts', function(data) {paragraphs = data['prophecies']});
          $.each(paragraphs, function(i, d) {
              p = $("#p-" + i);
              p.html("<p>" + d + "</p>")
  })
}
  </script>

  </head>

  <body>

    <div class="container">

        <h1 onclick ="set_content_in_divs({{ predictions }})">Что день {{ date }} готовит</h1>

        <div class="row">
            <div class="col" id="p-0">
            </div>
            <div class="col" id="p-1">
            </div>
            <div class="col" id="p-2">
            </div>
        </div>

        <div class="row">
            <div class="col" id="p-3">
            </div>
            <div class="col" id="p-4">
            </div>
            <div class="col" id="p-5">
            </div>
        </div>

    </div>
  </body>

</html>