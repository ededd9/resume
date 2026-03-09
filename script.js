async function updateVisitorCount() {
  const response = await fetch(
    "https://y8sl0igfie.execute-api.us-east-1.amazonaws.com/count",
  );
  const data = await response.json();
  document.getElementById("visitor-count").textContent = data.count;
}

updateVisitorCount();
