function publish_and_go_back() {

  var editor_css = editor.getValue();
  var editor_title = document.getElementById("title").value;

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      if(xhr.responseText == "1") {
        window.location.href = "/settings/themes"
      }
    }
  };
  xhr.open("POST", "/createtheme", true);
  xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  xhr.send(JSON.stringify({editor_css:editor_css,editor_title:editor_title}));
}

function publish() {
  var editor_css = editor.getValue();
  var editor_title = document.getElementById("title").value;

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      if(xhr.responseText == "1") {

        // TODO Message if success

      }
    }
  };
  xhr.open("POST", "/createtheme", true);
  xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  xhr.send(JSON.stringify({editor_css:editor_css,editor_title:editor_title}));
}

var docsExpanded = false;
function expandDocs(e) {
  console.log("expandDocs");
  if(docsExpanded) {
    e.parentNode.style.width="40px";
  } else {
    e.parentNode.style.width="640px";
  }
  docsExpanded = !docsExpanded;
}
