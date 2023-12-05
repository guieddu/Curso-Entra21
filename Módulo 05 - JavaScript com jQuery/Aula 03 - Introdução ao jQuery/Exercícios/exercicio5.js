$(document).ready(function () {
    const peopleTable = $("#peopleTable tbody");

    function fillTable() {
        people.forEach(function (person) {
            const row = $("<tr>").append(
                $("<td>").text(person.id),
                $("<td>").text(person.name),
                $("<td>").text(person.age),
                $("<td>").text(person.sex === "M" ? "Masculino" : "Feminino")
            );
            peopleTable.append(row);
        });
    }

    fillTable();
});