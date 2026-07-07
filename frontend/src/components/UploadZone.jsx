import { useDropzone } from "react-dropzone";
import { motion } from "framer-motion";
import { FaCloudUploadAlt } from "react-icons/fa";

function UploadZone({
  video,
  setVideo,
  uploadVideo,
  loading,
}) {

  const onDrop = (acceptedFiles) => {

    console.log("📂 Files:", acceptedFiles);

    if (acceptedFiles.length > 0) {

      console.log("✅ Selected:", acceptedFiles[0]);

      setVideo(acceptedFiles[0]);

    } else {

      console.log("❌ No file selected");

    }

  };

  const {
    getRootProps,
    getInputProps,
    isDragActive,
  } = useDropzone({
    accept: {
      "video/*": [],
    },
    multiple: false,
    noClick: false,
    onDrop,
  });

  return (

    <motion.div
      {...getRootProps()}
      whileHover={{ scale: 1.01 }}
      className="upload-zone"
    >

      <input {...getInputProps()} />

      <motion.div
        animate={{
          y: [0, -10, 0],
        }}
        transition={{
          repeat: Infinity,
          duration: 2,
        }}
      >
        <FaCloudUploadAlt size={75} />
      </motion.div>

      <h2>
        {isDragActive
          ? "Drop your video..."
          : "Drop your video here"}
      </h2>

      <p>or click to browse</p>

      <p>MP4 • MOV • AVI • MKV</p>

      {video && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="selected-video"
          style={{
            marginTop: 20,
            padding: 12,
            borderRadius: 12,
            background: "rgba(109,94,245,.12)",
            color: "#fff",
            fontWeight: 600,
          }}
        >
          📹 {video.name}
        </motion.div>
      )}

      <motion.button
        type="button"
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();

          console.log("🚀 Generate Clicked");
          console.log("Current Video:", video);

          uploadVideo();
        }}
        disabled={loading}
        className="generate-btn"
      >
        {loading
          ? "Generating..."
          : "✨ Generate AI Captions"}
      </motion.button>

    </motion.div>

  );
}

export default UploadZone;