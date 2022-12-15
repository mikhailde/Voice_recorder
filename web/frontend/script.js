let input = document.querySelector('input');
let form = document.querySelector('.u-form-spacing-15');
form.onsubmit = function(evt) {
    evt.preventDefault();
    eel.username(input.value);
    window.location = "http://localhost:8000/index.html";
  //   eel.recording(); // Call a Python function
  // setTimeout(() => eel.recording(), 10000);
};