$(document).ready(function () {
  $("#filetable").DataTable({
    paging: false,
    stateSave: true,
    info: false,
    language: {
      search: "Filtrar",
    },
  });
  document.getElementById("filetable_filter").style.color = "white"
});

$("#download-all").click(function (e) {
  e.preventDefault();
  var url = "{% url 'archivos:zip-ramo' current %}";
  $.get(url, function (data) {
    window.location.href = "/" + data["link"];
  });
});
