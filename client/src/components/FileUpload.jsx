
import React, { useState } from "react";
import axios from "axios";

function FileUpload() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:5000/upload", formData);
      setMessage(res.data.message || "Upload successful!");
    } catch (error) {
      setMessage("Upload failed.");
    }
  };

  return (
    <div className="w-full text-center">
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-2 block mx-auto"
      />
      <button
        onClick={handleUpload}
        className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Upload Excel
      </button>
      <p className={`mt-2 ${message.includes("failed") ? "text-red-600" : "text-green-600"}`}>
        {message}
      </p>
    </div>
  );
}

export default FileUpload;
