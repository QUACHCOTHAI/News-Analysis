function formatMarkdown(text) {
    return text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
}

async function analyze() {
    const input = document.getElementById("urlInput");
    const url = input.value.trim();
    const chatBox = document.getElementById("chat-box");

    if (!url) return;

    // Thêm tin nhắn người dùng
    const userBubble = document.createElement("div");
    userBubble.className = "bubble user-msg";
    userBubble.textContent = url;
    chatBox.appendChild(userBubble);

    // Thêm khung đang phân tích từ bot
    const botBubble = document.createElement("div");
    botBubble.className = "bubble bot-msg";
    botBubble.innerHTML = "<em>Đang phân tích...</em>";
    chatBox.appendChild(botBubble);

    chatBox.scrollTop = chatBox.scrollHeight;
    input.value = "";

    try {
        const res = await fetch("/analyze", {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });

        const data = await res.json();
        if (data.error) {
            botBubble.innerHTML = `<span style="color:red;">${data.error}</span>`;
        } else {
            botBubble.innerHTML = formatMarkdown(data.analysis);
        }
    } catch (err) {
        botBubble.innerHTML = `<span style="color:red;">Lỗi kết nối đến server.</span>`;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}
