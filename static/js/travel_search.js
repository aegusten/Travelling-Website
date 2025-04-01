const searchForm = document.getElementById('travel-search-form');
const searchUrl = searchForm.dataset.searchUrl;
const resultsContainer = document.getElementById('searchResultsContainer');

if (searchForm && resultsContainer && searchUrl) {
  searchForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(searchForm);
    const params = new URLSearchParams();
    for (const [key, value] of formData.entries()) {
      params.append(key, value);
    }

    console.log("🔍 Submitting search with params:", params.toString());

    fetch(`${searchUrl}?${params.toString()}`, { method: "GET" })
      .then(response => {
        if (!response.ok) throw new Error(`Server responded with ${response.status}`);
        return response.text();
      })
      .then(htmlSnippet => {
        resultsContainer.innerHTML = htmlSnippet;
        console.log("✅ Results loaded successfully.");
      })
      .catch(err => {
        console.error("❌ Search error:", err);
        resultsContainer.innerHTML = `
          <div style="color:red;">
            <h4>Failed to load results</h4>
            <p>Our system might be down. Please try again later.</p>
          </div>
        `;
      });
  });
}
