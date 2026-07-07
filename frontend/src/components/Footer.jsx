function Footer() {
  return (
    <footer
      style={{
        marginTop: 100,
        padding: "30px 0",
        textAlign: "center",
        color: "#94A3B8",
      }}
    >
      <h3>🦆 QuackVision AI</h3>

      <p style={{ marginTop: 10 }}>
        Powered by Gemma • Whisper • OCR • FastAPI • React
      </p>

      <p style={{ marginTop: 20, fontSize: 13 }}>
        Built for the AMD Developer Challenge
      </p>
    </footer>
  );
}

export default Footer;