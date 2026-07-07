import { motion } from "framer-motion";
import { FaPlayCircle } from "react-icons/fa";

function Hero() {
  return (
    <motion.section
      initial={{ opacity: 0, y: -40 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
      style={{
        textAlign: "center",
        padding: "80px 20px 50px",
        position: "relative",
        overflow: "visible",
      }}
    >
      {/* Animated Glow */}
      <motion.div
        animate={{
          scale: [1, 1.08, 1],
          opacity: [0.15, 0.22, 0.15],
        }}
        transition={{
          duration: 6,
          repeat: Infinity,
        }}
        style={{
          width: 420,
          height: 420,
          background:
            "radial-gradient(circle,#6D5EF5 0%,#4CC9F0 55%,transparent 75%)",
          filter: "blur(170px)",
          position: "absolute",
          top: -170,
          left: "50%",
          transform: "translateX(-50%)",
          zIndex: -1,
        }}
      />

      {/* Logo */}
      <motion.div
        animate={{
          y: [0, -8, 0],
          rotate: [0, 5, -5, 0],
        }}
        transition={{
          repeat: Infinity,
          duration: 4,
        }}
        style={{
          fontSize: 62,
          marginBottom: 18,
        }}
      >
        🦆
      </motion.div>

      {/* Title */}
      <h1
        style={{
          fontSize: "72px",
          fontWeight: 900,
          lineHeight: 1.2,
          margin: 0,
          marginBottom: 24,
          overflow: "visible",
          background:
            "linear-gradient(90deg,#6D5EF5,#4CC9F0,#22C55E)",
          WebkitBackgroundClip: "text",
          WebkitTextFillColor: "transparent",
          letterSpacing: "-2px",
        }}
      >
        QuackVision AI
      </h1>

      {/* Subtitle */}
      <p
        style={{
          maxWidth: 850,
          margin: "0 auto",
          color: "#94A3B8",
          fontSize: 22,
          lineHeight: 1.9,
        }}
      >
        AI-powered multilingual video understanding using Vision,
        OCR, Speech Recognition and Reasoning to generate
        platform-ready captions for Instagram, LinkedIn and YouTube.
      </p>

      {/* CTA */}
      <motion.button
        whileHover={{
          scale: 1.05,
          y: -3,
        }}
        whileTap={{
          scale: 0.96,
        }}
        style={{
          marginTop: 42,
          padding: "18px 58px",
          borderRadius: 18,
          border: "none",
          cursor: "pointer",
          background:
            "linear-gradient(90deg,#6D5EF5,#4CC9F0)",
          color: "#fff",
          fontWeight: 700,
          fontSize: 18,
          display: "inline-flex",
          alignItems: "center",
          gap: 12,
          boxShadow:
            "0 18px 45px rgba(109,94,245,.35)",
        }}
      >
        <FaPlayCircle />
        Start Captioning
      </motion.button>
    </motion.section>
  );
}

export default Hero;