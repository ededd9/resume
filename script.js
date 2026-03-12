async function updateVisitorCount() {
  const response = await fetch(
    "https://9igu91n17b.execute-api.us-east-1.amazonaws.com/count",
  );
  const data = await response.json();
  document.getElementById("visitor-count").textContent = data.count;
}

updateVisitorCount();
