<script>
function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();
  if (!message) return;

  const chatBox = document.getElementById("chatMessages");

  // Add user message
  const userMsg = document.createElement("div");
  userMsg.className = "message user";
  userMsg.innerText = message;
  chatBox.appendChild(userMsg);

  input.value = "";

  // Fake bot response (replace with API call later)
  setTimeout(() => {
    const botMsg = document.createElement("div");
    botMsg.className = "message bot";
    botMsg.innerText = "Thinking... 🤖";
    chatBox.appendChild(botMsg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }, 500);

  chatBox.scrollTop = chatBox.scrollHeight;
}
</script>