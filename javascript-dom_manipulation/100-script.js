document.addEventListener('DOMContentLoaded', () => {
  const list = document.querySelector('.my_list');
  const addItem = document.getElementById('add_item');
  const removeItem = document.getElementById('remove_item');
  const clearList = document.getElementById('clear_list');

  addItem.addEventListener('click', function () {
    const li = document.createElement('li');
    li.textContent = 'Item';
    list.appendChild(li);
  });

  removeItem.addEventListener('click', function () {
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });

  clearList.addEventListener('click', function () {
    list.innerHTML = '';
  });
});
