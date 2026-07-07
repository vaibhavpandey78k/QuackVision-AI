import { motion } from "framer-motion";
import {
  FaFileVideo,
  FaDatabase,
  FaFilm,
} from "react-icons/fa";

function formatFileSize(bytes) {

  if (bytes < 1024) return bytes + " B";

  if (bytes < 1024 * 1024)
    return (bytes / 1024).toFixed(1) + " KB";

  return (bytes / (1024 * 1024)).toFixed(2) + " MB";
}

function VideoPreview({ video }) {

  if (!video) return null;

  const url = URL.createObjectURL(video);

  return (

    <motion.div

      className="preview-card"

      initial={{ opacity: 0, x: -40 }}

      animate={{ opacity: 1, x: 0 }}

      transition={{ duration: .6 }}

      whileHover={{
        y: -5
      }}

    >

      <h2>

        🎥 Uploaded Video

      </h2>

      <video

        src={url}

        controls

        className="preview-video"

      />

      <div className="video-info">

        <div className="video-row">

          <FaFileVideo />

          <div>

            <small>Filename</small>

            <strong>{video.name}</strong>

          </div>

        </div>

        <div className="video-row">

          <FaDatabase />

          <div>

            <small>File Size</small>

            <strong>{formatFileSize(video.size)}</strong>

          </div>

        </div>

        <div className="video-row">

          <FaFilm />

          <div>

            <small>Format</small>

            <strong>{video.type}</strong>

          </div>

        </div>

      </div>

    </motion.div>

  );

}

export default VideoPreview;