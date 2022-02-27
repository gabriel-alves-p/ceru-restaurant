/* ------------------------------------ Code Credit https://www.codegrepper.com/code-examples/html/input+type%3Ddate+min+today */

var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1;
var yyyy = today.getFullYear();
if (dd < 10) {
    dd = '0' + dd
}
if (mm < 10) {
    mm = '0' + mm
}

today = yyyy + '-' + mm + '-' + dd;
document.getElementById("date").setAttribute("min", today);

/* ------------------------------------ End Credit */