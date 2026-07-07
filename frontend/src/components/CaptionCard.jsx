import { motion } from "framer-motion";
import CopyButton from "./CopyButton";

function CaptionCard({ title, text }) {

  return (

    <motion.div
      className="caption-card"
      initial={{ opacity: 0, y: 25 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.45 }}
      whileHover={{
        y: -8,
        scale: 1.01,
      }}
    >

      <div className="caption-header">

        <h2>{title}</h2>

        <CopyButton text={text} />

      </div>

      <div className="caption-body">

        {text}

      </div>

    </motion.div>

  );

}

export default CaptionCard;