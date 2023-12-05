$(document).ready(function () {
    $("#clicker").click(function () {
        $("#secret").toggle();
        $(this).text(function (i, text) {
            return text === "Esconder" ? "Mostrar" : "Esconder";
        });
    });
});