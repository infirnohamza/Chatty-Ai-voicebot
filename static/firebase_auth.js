document.addEventListener("DOMContentLoaded", function () {
    // Register form submit event
    document
      .getElementById("register-form")
      .addEventListener("submit", function (event) {
        event.preventDefault();
        var email = document.getElementById("register-email").value;
        var password = document.getElementById("register-password").value;
  
        // Add validation
        if (email.trim() === "" || password.trim() === "") {
          console.error("Email and password fields cannot be empty.");
          return;
        }
  
        firebase
          .auth()
          .createUserWithEmailAndPassword(email, password)
          .then((userCredential) => {
            console.log("User registered:", userCredential.user);
          })
          .catch((error) => {
            console.error("Error registering user:", error);
          });
      });
  
    // Login form submit event
    document
      .getElementById("login-form")
      .addEventListener("submit", function (event) {
        event.preventDefault();
        var email = document.getElementById("login-email").value;
        var password = document.getElementById("login-password").value;
  
        // Add validation
        if (email.trim() === "" || password.trim() === "") {
          console.error("Email and password fields cannot be empty.");
          return;
        }
  
        firebase
          .auth()
          .signInWithEmailAndPassword(email, password)
          .then((userCredential) => {
            console.log("User logged in:", userCredential.user);
            window.location.href = "/index";
          })
          .catch((error) => {
            console.error("Error logging in user:", error);
          });
      });
  });
  