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
  "Watching every frame...",
  "Understanding the story...",
  "Listening to speech...",
  "Reading on-screen text...",
  "Analyzing visual context...",
  "Generating intelligent captions...",
];

function AIProcessing({ completed }) {

  const [progress, setProgress] = useState(0);
  const [currentStep, setCurrentStep] = useState("Starting...");
  const [seconds, setSeconds] = useState(0);
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

  // Elapsed Timer
  useEffect(() => {

    const timer = setInterval(() => {

      setSeconds((prev) => prev + 1);

    }, 1000);

    return () => clearInterval(timer);

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
        Analysis Complete
      </h1>

      <p
        style={{
          textAlign: "center",
          color: "#94A3B8",
          fontSize: 18,
        }}
      >
        Opening AI Caption Studio...
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
        Analyzing Your Video
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

      <p
        style={{
          marginTop: 10,
          textAlign: "center",
          color: "#94A3B8",
          fontWeight: 600,
        }}
      >
        ⏱ {seconds}s elapsed
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

        <span>Typical processing time</span>

        <strong>30–90 seconds</strong>

      </div>

    </div>

  );
}

export default AIProcessing;