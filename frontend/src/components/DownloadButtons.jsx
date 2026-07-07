import jsPDF from "jspdf";
import {
  FaDownload,
  FaFilePdf,
  FaCopy,
  FaFileCode,
} from "react-icons/fa";

import { motion } from "framer-motion";
import toast from "react-hot-toast";

function DownloadButtons({ analysis }) {

  const copyAll = async () => {

    const text = `
FORMAL

${analysis.formal_caption}

----------------------------------

SARCASTIC

${analysis.sarcastic_caption}

----------------------------------

TECH

${analysis.humorous_tech_caption}

----------------------------------

MEME

${analysis.humorous_nontech_caption}

----------------------------------

SUMMARY

${analysis.summary}

----------------------------------

HASHTAGS

${analysis.hashtags.join(" ")}

----------------------------------

KEYWORDS

${analysis.keywords.join(", ")}

`;

    await navigator.clipboard.writeText(text);

    toast.success("Everything copied!");
  };

  const downloadTXT = () => {

    const blob = new Blob(
      [JSON.stringify(analysis, null, 2)],
      { type: "text/plain" }
    );

    const link = document.createElement("a");

    link.href = URL.createObjectURL(blob);

    link.download = "QuackVision_Report.txt";

    link.click();

    toast.success("TXT Downloaded");
  };

  const downloadPDF = () => {

    const pdf = new jsPDF();

    pdf.setFontSize(18);
    pdf.text("QuackVision AI Report",15,20);

    pdf.setFontSize(12);

    let y = 35;

    Object.entries(analysis).forEach(([key,value])=>{

      const text = Array.isArray(value)
      ? value.join(", ")
      : String(value);

      const lines = pdf.splitTextToSize(
        `${key.toUpperCase()}\n${text}`,
        170
      );

      pdf.text(lines,15,y);

      y += lines.length*7+10;

      if(y>270){

        pdf.addPage();

        y=20;

      }

    });

    pdf.save("QuackVision_Report.pdf");

    toast.success("PDF Downloaded");

  };

  const downloadJSON = ()=>{

    const blob=new Blob(

      [JSON.stringify(analysis,null,2)],

      {

        type:"application/json"

      }

    );

    const link=document.createElement("a");

    link.href=URL.createObjectURL(blob);

    link.download="QuackVision_Report.json";

    link.click();

    toast.success("JSON Downloaded");

  };

  return(

    <motion.div

      className="download-center"

      initial={{opacity:0,y:25}}

      animate={{opacity:1,y:0}}

    >

      <h2>

        📥 Export Your AI Report

      </h2>

      <p>

        Download or copy your AI generated insights.

      </p>

      <div className="download-grid">

        <button
          className="download-btn copy"
          onClick={copyAll}
        >

          <FaCopy/>

          Copy All

        </button>

        <button
          className="download-btn txt"
          onClick={downloadTXT}
        >

          <FaDownload/>

          TXT

        </button>

        <button
          className="download-btn json"
          onClick={downloadJSON}
        >

          <FaFileCode/>

          JSON

        </button>

        <button
          className="download-btn pdf"
          onClick={downloadPDF}
        >

          <FaFilePdf/>

          PDF

        </button>

      </div>

    </motion.div>

  );

}

export default DownloadButtons;