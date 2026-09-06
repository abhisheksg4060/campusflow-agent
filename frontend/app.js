async function handleRequest() {
  const message = document.getElementById("input").value;

  const response = await fetch("http://localhost:8000/agent", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  document.getElementById("output").innerText = data.response;
}