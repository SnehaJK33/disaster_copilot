// Auto-refresh dashboard every 60 seconds
setInterval(() => {
    fetch(window.location.href)
        .then(response => response.text())
        .then(html => {
            // Parse returned HTML and replace main content
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, "text/html");
            const newMain = doc.querySelector("main");
            const currentMain = document.querySelector("main");
            if (newMain && currentMain) {
                currentMain.innerHTML = newMain.innerHTML;
            }
        })
        .catch(err => console.error("Error refreshing dashboard:", err));
}, 60000); // refresh every 60 seconds
