const addItem = document.getElementById('add_item');

addItem.addEventListener('click', function () {
  const newItem = document.createElement('li');
  const newText = document.createTextNode('Item');
  newItem.appendChild(newText);
  document.querySelector('ul.my_list').appendChild(newItem);
});
