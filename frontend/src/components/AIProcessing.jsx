import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import {
  FaCheckCircle,
  FaSpinner,
} from "react-icons/fa";

import api from "../services/api";

const pipeline = [
  "🎥 Extracting Frames",
  "🖼 Detecting Key Scenes",
  "🔊 Extracting Audio",
  "🗣 Understanding Speech",
  "👁 Reading On-screen Text",
  "👀 Understanding Visual Context",
  "🧠 Understanding Story",
  "✨ Generating Captions",
  "✅ Completed",
];

const messages = [
  "🎬 Watching every important moment...",
  "🎙️ Listening carefully to every spoken word...",
  "👀 Looking beyond what meets the eye...",
  "🧠 Understanding the complete story...",
  "📝 Reading every important word on screen...",
  "🎨 Matching visuals with emotions...",
  "✨ Turning moments into meaningful captions...",
  "🤖 Our AI team is discussing the best captions...",
  "📖 Every great story deserves the perfect words...",
  "☕ Great captions take a little thinking...",
  "🚀 Almost there... polishing every detail...",
  "🦆 Thanks for your patience. You're going to love the result!"
];

function AIProcessing({ completed }) {

  const [progress, setProgress] = useState(0);
  const [currentStep, setCurrentStep] = useState("Starting...");
  const [messageIndex, setMessageIndex] = useState(0);

  // Backend Progress Polling
  useEffect(() => {

    const interval = setInterval(async () => {

      try {

        const res = await api.get("/api/progress");

        setProgress(res.data.progress);
        setCurrentStep(res.data.step);

      } catch (err) {

        console.log(err);

      }

    }, 500);

    return () => clearInterval(interval);

  }, []);


  // Rotating AI Messages
  useEffect(() => {

    const rotate = setInterval(() => {

      setMessageIndex((prev) => (prev + 1) % messages.length);

    }, 3000);

    return () => clearInterval(rotate);

  }, []);

  const currentIndex = pipeline.indexOf(currentStep);

  return (

    <div className="processing-card">

      {/* Animated Brain */}
      {
  completed ? (

    <>

      <motion.div
        initial={{ scale: 0.6, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ duration: 0.5 }}
        style={{
          fontSize: 70,
          textAlign: "center",
          marginBottom: 20,
        }}
      >
        🎉
      </motion.div>

      <h1
        style={{
          textAlign: "center",
        }}
      >
        🎉 Your Story Has Been Understood
      </h1>

      <p
        style={{
          textAlign: "center",
          color: "#94A3B8",
          fontSize: 18,
        }}
      >
        Preparing your personalized captions...
      </p>

    </>

  ) : (

    <>

      <motion.div
        animate={{
          scale: [1, 1.12, 1],
          rotate: [0, 4, -4, 0],
        }}
        transition={{
          repeat: Infinity,
          duration: 2.2,
        }}
        style={{
          fontSize: 60,
          textAlign: "center",
          marginBottom: 15,
        }}
      >
        🧠
      </motion.div>

      <h1>
      🦆 QuackVision AI is Understanding Your Story
      </h1>

      <motion.p
        key={messageIndex}
        initial={{ opacity: 0, y: 8 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.35 }}
      >
        {messages[messageIndex]}
      </motion.p>

    </>

  )
}

      {/* Progress Bar */}
      <div className="progress-bar">

        <motion.div
          className="progress-fill"
          animate={{
            width: `${progress}%`,
          }}
          transition={{
            duration: 0.45,
          }}
        />

      </div>

      {/* Percentage */}
      <motion.h2
        animate={{
          scale: [1, 1.05, 1],
        }}
        transition={{
          repeat: Infinity,
          duration: 1,
        }}
      >
        {progress}%
      </motion.h2>

      <p className="current-step">
        {currentStep}
      </p>

      {/* Pipeline */}
      <div className="pipeline">

        {pipeline.map((step, index) => (

          <div
            key={index}
            className="pipeline-step"
          >

            {index < currentIndex ? (

              <FaCheckCircle color="#22C55E" />

            ) : index === currentIndex ? (

              <motion.div
                animate={{
                  rotate: 360,
                }}
                transition={{
                  repeat: Infinity,
                  duration: 1,
                  ease: "linear",
                }}
              >
                <FaSpinner color="#6D5EF5" />
              </motion.div>

            ) : (

              <div className="dot" />

            )}

            <span>{step}</span>

          </div>

        ))}

      </div>

      <div className="estimate">

  <span>
    🦆 QuackVision analyzes Speech, Vision and OCR before generating captions.
  </span>

  <strong>
    Every video is understood before a single caption is written.
  </strong>

</div>
    <motion.p
  key={messageIndex + "-fact"}
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  transition={{ duration: 0.5 }}
  style={{
    marginTop: 25,
    textAlign: "center",
    color: "#94A3B8",
    fontSize: 14,
    lineHeight: 1.6,
  }}
>
  💡 Every caption is created by combining speech, visual understanding and on-screen text.
</motion.p>

    </div>

  );
}

export default AIProcessing;