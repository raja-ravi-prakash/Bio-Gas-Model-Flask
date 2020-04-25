mdc.ripple.MDCRipple.attachTo(document.querySelector(".button"));

function run() {
  let year = document.getElementById("year").value;
  let month = document.getElementById("month").value;
  let day = document.getElementById("day").value;
  var http = new XMLHttpRequest();
  var url = window.location.href + "data";
  http.open("POST", url, true);
  http.setRequestHeader("Content-type", "application/json");

  http.onreadystatechange = function () {
    if (http.readyState == 4 && http.status == 200) {
      materialAlert(
        "Result",
        "INR <strong>" + http.responseText.substring(0, 5) + "</strong>",
        () => {}
      );
    }
  };
  var data = JSON.stringify({ month: month, year: year, day: day });
  http.send(data);
}
