var values = document.getElementsByTagName("li");
var i = 0;

document.getElementById('b').addEventListener('click', function(){
  var list = document.createElement('li');
  var text = document.createTextNode('WORD');
  list.appendChild(text);
  document.getElementById('thelist').appendChild(list);
  list.addEventListener('mouseover', function(x) {
    document.getElementById('h').innerHTML = x.target.innerHTML;
  });
  list.addEventListener('click', function(x) {
    x.target.remove();
  });
});

//for (var i = 0; i < values.length; i++) {
while(i < values.length) {
	values[i].addEventListener('mouseover', function(x) {
    document.getElementById('h').innerHTML = x.target.innerHTML;
  });
  values[i].addEventListener('click', function(x) {
    x.target.remove();
  });
  i++;
}

document.getElementById('thelist').addEventListener('mouseleave', function(){
  document.getElementById('h').innerHTML = "Hello World!";
});

var fib = [];

document.getElementById('fb').addEventListener('click', function(){
  if (fib.length <= 1) {
    var list = document.createElement('li');
    var text = document.createTextNode('1');
    list.appendChild(text);
    document.getElementById('fiblist').appendChild(list);
    fib.push(list.innerHTML);
  }
  else {
    var list = document.createElement('li');
    var text = document.createTextNode(Number(fib[fib.length-1]) + Number(fib[fib.length-2]));
    list.appendChild(text);
    document.getElementById('fiblist').appendChild(list);
    fib.push(list.innerHTML);
  }
});
