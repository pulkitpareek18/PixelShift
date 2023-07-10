const selectMe = (element) =>{
    Array.from(document.getElementsByClassName("btn btn-info btn-sq-responsive")).forEach(e=>{
     e.classList.remove("btn-danger")
     e.classList.remove("active")
    })
    element.classList.add("active")
    element.classList.add("btn-danger")
    document.getElementById('imageFormatInput').value = element.dataset.convert
   }

   function showToast(message,backgroundClass) {
     // Create a div element for the toast
     var toastDiv = document.createElement("div");
     toastDiv.setAttribute("class", `toast show text-bg-${backgroundClass}`);
     toastDiv.setAttribute("style", "position: absolute;");
     toastDiv.setAttribute("role", "alert");
     toastDiv.setAttribute("aria-live", "assertive");
     toastDiv.setAttribute("aria-atomic", "true");
   
     // Create a div element for the toast body
     var toastBodyDiv = document.createElement("div");
     toastBodyDiv.setAttribute("class", "toast-body");
     toastBodyDiv.innerHTML = message;
   
           
           
     // Append the toast body to the toast
     toastDiv.appendChild(toastBodyDiv);
   
     // Append the alert container to the document body
     document.getElementById("alert").appendChild(toastDiv);
   }
   

   
   let spinner = document.getElementById("spinner")

   $("form#data").submit(function(e) {
     Pace.restart()
     spinner.style.display = "inline-block"
     e.preventDefault();    
     var formData = new FormData(this);
     let alertContainer = document.getElementById('alert')
     alertContainer.innerHTML = ""
 
     $.ajax({
         url: "/api/convert",
         type: 'POST',
         data: formData,
         success: function (data) {
           alertContainer.innerHTML = data
           spinner.style.display = "none"
         },
         fail: function(){
          alertContainer.innerHTML = `<div class="toast show align-items-center text-bg-danger border-0" role="alert" aria-live="assertive" aria-atomic="true">
          <div class="d-flex">
              <div class="toast-body">
              No Internet Connection.
              </div>
              <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
          </div>`   
              },
         cache: false,
         contentType: false,
         processData: false
     });
   });