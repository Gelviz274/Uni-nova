const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

function previewFiles(type) {
  let files = document.getElementById(type).files;
  let previewContainer = type === 'imagenes' ? document.getElementById('imagePreviews') : document.getElementById('videoPreviews');
  previewContainer.innerHTML = '';

  for (let i = 0; i < files.length; i++) {
      let file = files[i];
      let reader = new FileReader();
      reader.onload = function(e) {
          let previewElement;
          if (type === 'imagenes') {
              previewElement = document.createElement('img');
              previewElement.src = e.target.result;
              previewElement.style.maxWidth = '100px';
              previewElement.style.margin = '10px';
          } else if (type === 'videos') {
              previewElement = document.createElement('video');
              previewElement.src = e.target.result;
              previewElement.controls = true;
              previewElement.style.maxWidth = '100px';
              previewElement.style.margin = '10px';
          }
          previewContainer.appendChild(previewElement);
      };
      reader.readAsDataURL(file);
  }
}

function validateForm() {
  let nombreProyecto = document.getElementById('nombre_proyecto').value;
  let descripcion = document.getElementById('descripcion').value;
  let videos = document.getElementById('videos').files.length;
  let imagenes = document.getElementById('imagenes').files.length;

  if (!nombreProyecto || !descripcion || (!videos && !imagenes)) {
      alert('Por favor, complete todos los campos y asegúrese de subir al menos una imagen o video.');
      return false;
  }
  return true;
}