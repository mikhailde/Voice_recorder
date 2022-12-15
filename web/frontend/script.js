let input = document.querySelector('input');
let form = document.querySelector('.u-form-spacing-15');
form.onsubmit = function(evt) {
    evt.preventDefault();
    eel.print(input.value);
    // eel.recording(); // Call a Python function
	// setTimeout(() => eel.recording(), 10000);
  };
  