const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});


$(document).ready(function(){
  $('#registro-form').submit(function(event){
      event.preventDefault();
      $.ajax({
          type: 'POST',
          url: '/registrarse/',
          data: $('#registro-form').serialize(),
          success: function(response){
              if (response.success) {
                  $('#mensaje').html('<div class="alert alert-success">' + response.mensaje + '</div>');
              } else {
                  $('#mensaje').html('<div class="alert alert-danger">' + response.mensaje + '</div>');
              }
          },
          error: function(xhr, errmsg, err){
              $('#mensaje').html('<div class="alert alert-danger">Error: ' + xhr.status + ": " + xhr.responseText + '</div>');
          }
      });
  });
});