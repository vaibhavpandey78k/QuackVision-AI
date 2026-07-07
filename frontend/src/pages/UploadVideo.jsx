import { useState, useRef, useEffect } from "react";
import { motion } from "framer-motion";
import api from "../services/api";

import Hero from "../components/Hero";
import UploadZone from "../components/UploadZone";
import AIProcessing from "../components/AIProcessing";
import CaptionCard from "../components/CaptionCard";
import DownloadButtons from "../components/DownloadButtons";
import Footer from "../components/Footer";
import VideoPreview from "../components/VideoPreview";
import InsightsPanel from "../components/InsightsPanel";

function UploadVideo() {

  const [video, setVideo] = useState(null);
  const [message, setMessage] = useState("");
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [completed, setCompleted] = useState(false);

  const resultsRef = useRef(null);

  // Auto Scroll to Results
  useEffect(() => {

    if (analysis && resultsRef.current) {

      setTimeout(() => {

        resultsRef.current.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });

      }, 300);

    }

  }, [analysis]);

  const uploadVideo = async () => {

    if (!video) {
      alert("Please select a video first.");
      return;
    }

    setLoading(true);
    setCompleted(false);
    setMessage("");
    setAnalysis(null);

    const formData = new FormData();
    formData.append("file", video);

    try {

      const response = await api.post("/api/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setMessage("✨ AI Analysis Completed Successfully");

      setAnalysis(response.data.pipeline.analysis);

      setCompleted(true);

      setTimeout(() => {

        setLoading(false);
        setCompleted(false);

      }, 1800);

    }

    catch (err) {

      console.error(err);

      setLoading(false);

      setMessage("❌ Upload Failed");

    }

  };

  return (

    <div className="section">

      <Hero />

      <UploadZone
        video={video}
        setVideo={setVideo}
        uploadVideo={uploadVideo}
        loading={loading}
      />

      {loading && (

        <AIProcessing
          completed={completed}
        />

      )}

      {message && (

<motion.div

initial={{opacity:0,y:-20}}

animate={{opacity:1,y:0}}

transition={{duration:.5}}

className={
message.includes("Failed")
?
"error-banner"
:
"success-banner"
}

>

{message}

</motion.div>

)}

      

      {analysis && (

        <div ref={resultsRef}>

          <div
            className="dashboard-grid"
            style={{
              marginTop: 50,
            }}
          >

            <VideoPreview
              video={video}
            />

            <InsightsPanel
              analysis={analysis}
            />

          </div>

          <div className="caption-studio">

            <h1 className="caption-title">

              🎬 AI Caption Studio

            </h1>

            <CaptionCard
              title="🎓 Formal Caption"
              text={analysis.formal_caption}
            />

            <CaptionCard
              title="😏 Sarcastic Caption"
              text={analysis.sarcastic_caption}
            />

            <CaptionCard
              title="🤖 Tech Caption"
              text={analysis.humorous_tech_caption}
            />

            <CaptionCard
              title="😂 Meme Caption"
              text={analysis.humorous_nontech_caption}
            />

            <CaptionCard
              title="📄 Summary"
              text={analysis.summary}
            />

            <CaptionCard
              title="🔥 Hashtags"
              text={analysis.hashtags.join(" ")}
            />

            <CaptionCard
              title="🔑 SEO Keywords"
              text={analysis.keywords.join(", ")}
            />

          </div>

          <DownloadButtons
            analysis={analysis}
          />

        </div>

      )}

      <Footer />

    </div>

  );

}

export default UploadVideo;