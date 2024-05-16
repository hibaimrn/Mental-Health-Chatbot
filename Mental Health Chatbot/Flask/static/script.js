document.getElementById("chat-form").onsubmit = function(event) {
    event.preventDefault();
    var userQuery = document.getElementById("user-input").value;
    document.getElementById("user-input").value = "";
  
    document.getElementById("chat-box").innerHTML += "<p class='you'><strong>You:</strong> " + userQuery + "</p>";
  
    fetch("/get_response", {
      method: "POST",
      body: new URLSearchParams({
        user_query: userQuery
      })
    })
    .then(response => response.text())
    .then(data => {
      document.getElementById("chat-box").innerHTML += "<p class='bot'><strong>Bot:</strong> " + data + "</p>";
    });
  };
  