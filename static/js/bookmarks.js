function remove_bookmark_slot(e) {
  e.parentNode.parentNode.remove()
}

function remove_category(e) {
  e.parentNode.parentNode.remove()
}

function add_bookmark_slot(e) {
  e.parentNode.parentNode.insertBefore(create_bookmark_container(), e.parentNode);
  $('.bookmark').arrangeable();
}

function add_category_slot(e) {
    var d1 = document.createElement("div");
    d1.className = "category";

    var i1 = document.createElement("input");
    i1.type = "text"
    i1.placeholder = "Category title"
    i1.className = "categorytitle"

    var d2 = document.createElement("div");
    d2.className = "bookmark_menu";

    var r = document.createElement("div");
    r.className = "bookmark_menu_item";
    r.innerHTML = '<i class="fa fa-trash" aria-hidden="true"></i>'
    r.onclick = function () {
      remove_category(this)
    };

    var a = document.createElement("div");
    a.className = "bookmark_menu_item";
    a.innerHTML = '<i class="fa fa-plus" aria-hidden="true"></i>'
    a.onclick = function () {
      add_bookmark_slot(this)
    };

    d2.appendChild(r);
    d2.appendChild(a);

    d1.appendChild(i1);
    d1.appendChild(create_bookmark_container());
    d1.appendChild(d2);

    e.parentNode.insertBefore(d1, e);

    $('.category').arrangeable();
}

function create_bookmark_container() {
  var d = document.createElement("div");
  d.className = "bookmark";

  var i1 = document.createElement("input");
  i1.type = "text"
  i1.placeholder = "Title"
  var i2 = document.createElement("input");
  i2.type = "text"
  i2.placeholder = "URL"
  var r = document.createElement("div");
  r.className = "remove_bookmark";
  r.innerHTML = '<i class="fa fa-times" aria-hidden="true"></i>'
  r.onclick = function () {
    remove_bookmark_slot(this);
  };

  d.appendChild(i1)
  d.appendChild(i2)
  d.appendChild(r)

  return d
}

function save_bookmarks() {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/bookmarks", true);
  xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  xhr.send(generate_json());
}

function generate_json() {

  var json = "{"

  var bookmarks = document.getElementsByClassName("bookmarks");

  if (bookmarks.length == 1) {
    bookmarks = bookmarks[0]
  } else {
    return
  }

  for (var i = 0; i < bookmarks.getElementsByClassName("category").length; i++) {
    var category = bookmarks.getElementsByClassName("category")[i]

    categorytitle = category.getElementsByClassName("categorytitle")
    if (categorytitle.length == 1) {
      categorytitle = categorytitle[0]
    } else {
      break
    }

    if(categorytitle.value == "") {
      categorytitle.style.borderBottom = "2px solid rgba(255,0,0,0.5)"
      if(json[json.length-1] == ",") {
        json = json.slice(0, -1);
      }
      continue
    }

    json += '\"'+categorytitle.value+'\":{'

    for (var j = 0; j < category.getElementsByClassName("bookmark").length; j++) {
      bookmark = category.getElementsByClassName("bookmark")[j]

      var inputs = bookmark.getElementsByTagName('input')

      var bookmarktitle = inputs[0]
      var bookmarkurl = inputs[1]

      if(bookmarktitle.value == "" || bookmarkurl.value == "") {
        if(bookmarktitle.value == "") {
          bookmarktitle.style.borderBottom = "2px solid rgba(255,0,0,0.5)"
        }
        if(bookmarkurl.value == "") {
          bookmarkurl.style.borderBottom = "2px solid rgba(255,0,0,0.5)"
        }

        if(json[json.length-1] == ",") {
          json = json.slice(0, -1);
        }
        continue
      }

      json += '\"'+bookmarktitle.value+'\":\"'+bookmarkurl.value+'\"'

      if (j < category.getElementsByClassName("bookmark").length-1) {
        json += ","
      }
    }
    json += "}"

    if (i < bookmarks.getElementsByClassName("category").length-1) {
      json += ","
    }
  }
  json += "}"

  return json
}
