const password_field = document.getElementById("password");
const confirm_password_field = document.getElementById("confirm-password");

confirm_password_field.addEventListener("blur", (e) => {
  e.preventDefault();
  if (password_field.value != confirm_password_field.value) {
    confirm_password_field.setCustomValidity("Password does not match");
  } else {
    confirm_password_field.setCustomValidity("");
  }
});

password_field.addEventListener("blur", (e) => {
  e.preventDefault();
  if (password_field.value != confirm_password_field.value) {
    confirm_password_field.setCustomValidity("Password does not match");
  } else {
    confirm_password_field.setCustomValidity("");
  }
});
