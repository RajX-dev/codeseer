import { useState } from "react";

/* ---------- helpers ---------- */
const getFileName = (path) => {
  if (!path) return "";
  return path.split("\\").pop().split("/").pop();
};

const clampText = (text, max = 120) => {
  if (!text) return "";
  return text.length > max ? text.slice(0, max) + "…" : text;
};

const confidenceStyle = (confidence) => {
  switch (confidence) {
    case "high":
      return { background: "#16a34a" };
    case "medium":
      return { background: "#ca8a04" };
    default:
      return { background: "#dc2626" };
  }
};

/* ---------- app ---------- */
function App() {
  const [results, setResults] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const runSearch = () => {
    if (!query.trim()) {
      alert("Please enter a search query");
      return;
    }

    setLoading(true);

    fetch("http://localhost:8000/api/v1/search/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query,
        top_k: 3,
        debug: false,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        setResults(data);
      })
      .catch((err) => {
        console.error(err);
      })
      .finally(() => {
        setLoading(false);
      });
  };

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
          disabled={loading}
          style={{ marginLeft: "10px", padding: "8px 12px" }}
        >
          {loading ? "Searching…" : "Search"}
        </button>
      </div>

      {loading && <p>Searching…</p>}

      {!loading && results.length === 0 ? (
        <p>No results found. Try a different query.</p>
      ) : (
        <ul style={{ listStyle: "none", padding: 0 }}>
          {results.map((item) => (
            <li
              key={item.rank}
              style={{
                marginBottom: "20px",
                padding: "14px",
                borderRadius: "8px",
                background: "#1f2937",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between" }}>
                <strong>{getFileName(item.file_path)}</strong>
                <span
                  style={{
                    color: "white",
                    padding: "2px 8px",
                    borderRadius: "999px",
                    fontSize: "12px",
                    ...confidenceStyle(item.confidence),
                  }}
                >
                  {item.confidence}
                </span>
              </div>

              <div
                style={{
                  marginTop: "8px",
                  fontFamily: "monospace",
                  whiteSpace: "pre-wrap",
                }}
              >
                {clampText(item.preview)}
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
