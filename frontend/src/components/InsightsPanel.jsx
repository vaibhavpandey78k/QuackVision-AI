import {
  FaLanguage,
  FaSmile,
  FaTags,
  FaCheckCircle,
  FaBrain,
} from "react-icons/fa";

import { motion } from "framer-motion";

import ConfidenceRing from "./ConfidenceRing";

function InsightsPanel({ analysis }) {

  if (!analysis) return null;

  return (

    <motion.div
      className="insights-card"
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: .6 }}
    >

      <h2>

        <FaBrain />

        AI Insights

      </h2>

      <ConfidenceRing
        value={analysis.confidence_score}
      />

      <div className="insight-item">

        <FaLanguage />

        <div>

          <small>Detected Language</small>

          <strong>{analysis.detected_language}</strong>

        </div>

      </div>

      <div className="insight-item">

        <FaSmile />

        <div>

          <small>Overall Mood</small>

          <strong>{analysis.overall_mood}</strong>

        </div>

      </div>

      <div className="insight-item">

        <FaTags />

        <div>

          <small>Video Category</small>

          <strong>{analysis.video_category}</strong>

        </div>

      </div>

      <div className="divider"/>

      <div className="ai-stack">

        <div>

          <FaCheckCircle color="#22C55E"/>

          Vision

        </div>

        <div>

          <FaCheckCircle color="#22C55E"/>

          OCR

        </div>

        <div>

          <FaCheckCircle color="#22C55E"/>

          Speech

        </div>

        <div>

          <FaCheckCircle color="#22C55E"/>

          Reasoning

        </div>

      </div>

    </motion.div>

  );

}

export default InsightsPanel;