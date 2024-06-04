document.addEventListener('DOMContentLoaded', function() {
  const passwordInput = document.getElementById('password');
  const confirmPasswordInput = document.getElementById('confirm_password');
  const errorMessage = document.getElementById('password-error');

  function validatePasswords() {
      const password = passwordInput.value;
      const confirmPassword = confirmPasswordInput.value;

      if (password.length >= 8 && confirmPassword.length >= 8 && password === confirmPassword) {
          errorMessage.style.display = 'none';
      } else {
          errorMessage.style.display = 'block';
      }
  }

  passwordInput.addEventListener('input', validatePasswords);
  confirmPasswordInput.addEventListener('input', validatePasswords);

  window.togglePassword = function(fieldId) {
      const field = document.getElementById(fieldId);
      if (field.type === "password") {
          field.type = "text";
      } else {
          field.type = "password";
      }
  }

  const signInBtn = document.getElementById('sign-in-btn');
  const signUpBtn = document.getElementById('sign-up-btn');
  const container = document.querySelector('.container');

  if (signInBtn && signUpBtn && container) {
      signUpBtn.addEventListener("click", () => {
          container.classList.add("sign-up-mode");
      });

      signInBtn.addEventListener("click", () => {
          container.classList.remove("sign-up-mode");
      });
  }
});