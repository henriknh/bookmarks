function preview_theme(preview_id=null) {

  if (preview_id == null) {
    var editor_css = editor.getValue();
    var editor_title = document.getElementById("title").value;
  }

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      if(xhr.responseText == "1") {
        window.location.href = "/preview";
      }
    }
  };
  xhr.open("POST", "/preview", true);
  xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  if (preview_id != null) {
    console.log("preview_id != null");
    xhr.send(JSON.stringify({preview_id:preview_id}));
  } else {
    console.log("preview_id == null");
    xhr.send(JSON.stringify({editor_css:editor_css,editor_title:editor_title}));
  }
}

function use_theme(theme_id) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      if(xhr.responseText == "1") {
        window.location.href = "/settings/themes";
        // TODO Success message
      }
    }
  };
  xhr.open("POST", "/theme", true);
  xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  xhr.send(JSON.stringify({theme_id:theme_id}));
}

function create_theme() {
  edit_theme();
}

function edit_theme(editor_id=null) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      if(xhr.responseText == "1") {
        window.location.href = "/editor";
      }
    }
  };
  xhr.open("POST", "/editor", true);
  xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  if (editor_id == null) {
    xhr.send(JSON.stringify({}));
  } else {
    xhr.send(JSON.stringify({editor_id:editor_id}));
  }
}

function remove_theme(theme_id, title) {

  console.log("asd");
  var result = confirm("Do you want to delete "+title+"?");
  if (!result) {
    return
  }

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      if(xhr.responseText == "1") {
        window.location.href = "/settings/themes";
        // TODO Success message
      }
    }
  };
  xhr.open("DELETE", "/theme", true);
  xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  xhr.send(JSON.stringify({theme_id:theme_id}));
}
