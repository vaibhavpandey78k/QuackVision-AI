import { useState } from "react";
import api from "../services/api";

function UploadVideo() {
  const [video, setVideo] = useState(null);
  const [message, setMessage] = useState("");

  const uploadVideo = async () => {
    if (!video) {
      alert("Please select a video first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", video);

    try {
      const response = await api.post("/api/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      console.log("✅ Upload Success:", response.data);

      setMessage(`✅ ${response.data.message}`);
    } catch (error) {
      console.error("❌ Upload Error:", error);

      if (error.response) {
        console.log("Status:", error.response.status);
        console.log("Response:", error.response.data);

        setMessage(
          `❌ Backend Error: ${
            error.response.data.detail ||
            JSON.stringify(error.response.data)
          }`
        );
      } else if (error.request) {
        console.log("No response received:", error.request);
        setMessage("❌ Server did not respond.");
      } else {
        console.log("Request Error:", error.message);
        setMessage(`❌ ${error.message}`);
      }
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>QuackVision AI</h1>

      <input
        type="file"
        accept="video/*"
        onChange={(e) => setVideo(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={uploadVideo}>
        Upload Video
      </button>

      <br />
      <br />

      <h3>{message}</h3>
    </div>
  );
}

export default UploadVideo;