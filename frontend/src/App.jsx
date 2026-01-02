import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadCV = async () => {
    if (!file) return alert("Upload a CV");

    const formData = new FormData();
    formData.append("cv", file);

    setLoading(true);

    try {
      // Send to Node.js server
      const res = await axios.post("http://localhost:5000/upload", formData);
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Resume processing failed");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <div className="left">
        <h1>Land Your Dream Job<br />with a Professional CV</h1>
        <p>3x Higher Interview Callback Rate Guaranteed</p>
      </div>

      <div className="right">
        <div className="upload-box">
          <input
            type="file"
            accept=".pdf,.doc,.docx"
            onChange={(e) => setFile(e.target.files[0])}
          />
          <button onClick={uploadCV}>
            {loading ? "Processing..." : "Upload CV"}
          </button>
        </div>

        {result && (
          <div className="result">
            <h3>Resume Summary</h3>
            <p>{result.summary}</p>

            <h3>Skills</h3>
            <ul>
              {result.skills.map((skill, i) => (
                <li key={i}>{skill}</li>
              ))}
            </ul>

            <h3>Interview Questions</h3>
            <ul>
              {result.questions.map((q, i) => (
                <li key={i}>{q}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
