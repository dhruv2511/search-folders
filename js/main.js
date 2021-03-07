
var file = "file://files/test.txt"

function readFile(file) {
  var request = new XMLHttpRequest();

  request.open("post", file, true);
  request.send();

  request.onreadystatechange = function () {
    if (request.readyState === 4) {
      console.log(request)
    }
  };
}
