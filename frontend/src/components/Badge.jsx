import { motion } from "framer-motion";

function Badge({ icon, label }) {
  return (
    <motion.div
      whileHover={{ scale: 1.05 }}
      transition={{ duration: 0.2 }}
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "8px",
        padding: "10px 18px",
        background: "#1B2437",
        border: "1px solid rgba(255,255,255,.08)",
        borderRadius: "999px",
        color: "#F8FAFC",
        fontWeight: 600,
        fontSize: "14px",
        marginRight: "12px",
        marginBottom: "12px",
        boxShadow: "0 10px 25px rgba(0,0,0,.25)",
      }}
    >
      <span style={{ fontSize: "18px" }}>{icon}</span>
      <span>{label}</span>
    </motion.div>
  );
}

export default Badge;