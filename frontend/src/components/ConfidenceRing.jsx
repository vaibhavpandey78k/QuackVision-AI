import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

function ConfidenceRing({ value }) {
  return (
    <div
      style={{
        width: 180,
        margin: "auto",
      }}
    >
      <CircularProgressbar
        value={value}
        text={`${value}%`}
        strokeWidth={8}
        styles={buildStyles({
          pathColor: "#6D5EF5",
          trailColor: "#1E293B",
          textColor: "#FFFFFF",
          textSize: "18px",
        })}
      />

      <h3
        style={{
          textAlign: "center",
          marginTop: 20,
        }}
      >
        AI Confidence
      </h3>
    </div>
  );
}

export default ConfidenceRing;