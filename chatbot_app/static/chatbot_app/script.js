function sendMessage() {
    var userInput = document.getElementById("user_input").value;
    document.getElementById("user_input").value = ""; // Clear input field

    // Update chat window
    var chatWindow = document.getElementById("chat-window");
    var userParagraph = document.createElement("p");
    userParagraph.textContent = "You: " + userInput;
    userParagraph.style.backgroundColor = "#dcf8c6";
    userParagraph.style.alignSelf = "flex-end";
    chatWindow.appendChild(userParagraph);

    // AJAX request to backend
    $.ajax({
        url: '/send_message/', // Backend URL
        type: 'POST',
        data: { message: userInput },
        success: function(response) {
            var aiParagraph = document.createElement("p");
            aiParagraph.textContent = "Chatbot: " + response.message;
            aiParagraph.style.backgroundColor = "#ffffff";
            chatWindow.appendChild(aiParagraph);
        },
        error: function(error) {
            console.log("Error:", error);
        }
    });
}


function setTask() {
    var newTask = document.getElementById("new_task").value;
    document.getElementById("new_task").value = ""; // Clear input field

    // Update task on frontend
    document.getElementById("task").innerHTML = "Task: " + newTask;

    $.ajax({
        url: '/send_message/', // Backend URL
        type: 'POST',
        data: { new_task: newTask },
        success: function(response) {
            console.log(response.message)
        },
        error: function(error) {
            console.log("Error:", error);
        }
    });
}

