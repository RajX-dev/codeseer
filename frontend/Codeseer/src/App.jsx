import { useEffect, useState } from "react";

function App() {
  // 1️⃣ State
  const [results, setResults] = useState([]);
  const [query, setQuery] = useState("");

  // 2️⃣ Search function
  const runSearch = () => {
    fetch("http://localhost:8000/api/v1/search/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: query || "test",
        top_k: 3,
        debug: false,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        setResults(data);
      })
      .catch((err) => {
        console.error("Error:", err);
      });
  };

  // 3️⃣ Run once on page load
  useEffect(() => {
    runSearch();
  }, []);

  // 4️⃣ UI
  return (
    <div style={{ padding: "40px", fontFamily: "sans-serif" }}>
      <h1>CodeSeer</h1>

      <div style={{ marginBottom: "20px" }}>
        <input
          type="text"
          placeholder="Search code..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{ padding: "8px", width: "300px" }}
        />
        <button
          onClick={runSearch}
          style={{ marginLeft: "10px", padding: "8px 12px" }}
        >
          Search
        </button>
      </div>

      {results.length === 0 ? (
        <p>No results yet.</p>
      ) : (
        <ul>
          {results.map((item) => (
            <li key={item.rank} style={{ marginBottom: "20px" }}>
              <div>
                <strong>Rank:</strong> {item.rank}
              </div>
              <div>
                <strong>File:</strong> {item.file_path}
              </div>
              <div>
                <strong>Confidence:</strong> {item.confidence}
              </div>
              <div>
                <strong>Preview:</strong> {item.preview}
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
