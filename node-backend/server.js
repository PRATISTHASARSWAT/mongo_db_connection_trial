const express = require("express");
const multer = require("multer");
const axios = require("axios");
const mongoose = require("mongoose");
const cors = require("cors");
const FormData = require("form-data");

const app = express();

/* -------------------- MIDDLEWARE -------------------- */
app.use(cors());
app.use(express.json());

/* -------------------- MONGODB -------------------- */
mongoose
  .connect("mongodb://127.0.0.1:27017/resume_ai")
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.error("MongoDB error:", err));

/* -------------------- SCHEMA -------------------- */
const ResumeSchema = new mongoose.Schema({
  filename: String,
  extracted_text: String,
  skills: [String],
  questions: [String],
  createdAt: { type: Date, default: Date.now }
});

const Resume = mongoose.model("Resume", ResumeSchema);

/* -------------------- MULTER -------------------- */
const upload = multer({
  storage: multer.memoryStorage()
});

/* -------------------- ROUTES -------------------- */

// Health check
app.get("/", (req, res) => {
  res.send("Resume AI Backend is running 🚀");
});

// Upload resume
app.post("/upload", upload.single("cv"), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: "No file uploaded" });
    }

    // Send file to FastAPI
    const formData = new FormData();
    formData.append("file", req.file.buffer, {
      filename: req.file.originalname,
      contentType: req.file.mimetype
    });

    const aiResponse = await axios.post(
      "http://127.0.0.1:8000/parse-resume/",
      formData,
      {
        headers: formData.getHeaders()
      }
    );

    const { text, skills, questions } = aiResponse.data;

    // Save to MongoDB
    const resumeDoc = new Resume({
      filename: req.file.originalname,
      extracted_text: text || "",
      skills: skills || [],
      questions: questions || []
    });

    await resumeDoc.save();

    res.json({
      message: "Resume processed and saved successfully ✅",
      data: resumeDoc
    });

  } catch (err) {
    console.error("UPLOAD ERROR:", err.message);
    res.status(500).json({ error: "Resume processing failed" });
  }
});

// Fetch all resumes (optional, for UI)
app.get("/resumes", async (req, res) => {
  try {
    const resumes = await Resume.find().sort({ createdAt: -1 });
    res.json(resumes);
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch resumes" });
  }
});

/* -------------------- SERVER -------------------- */
const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Node server running on http://localhost:${PORT}`);
});
