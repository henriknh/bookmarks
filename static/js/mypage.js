function searchInput(e) {

  if( !e ) e = window.event; // <---needed this --- and this ->--+

  if(e.keyCode == 13) {
    if(e.shiftKey){
      search(true)
    } else {
      search()
    }
  }
}
function search(shift=false) {
  var search = document.getElementById('search').value
  if(shift) {
    var tarea_regex = /(http(s?))\:\/\//gi;
    if(!tarea_regex.test(search)) {
      search = 'http://'+search
    }
    window.location.replace(search);
  } else {
    window.location.replace('https://www.google.se/search?q='+search);
  }
}
