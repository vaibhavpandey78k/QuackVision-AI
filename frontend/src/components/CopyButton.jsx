import { FaCopy, FaCheck } from "react-icons/fa";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import toast from "react-hot-toast";

function CopyButton({ text }) {

  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {

    try{

      await navigator.clipboard.writeText(text);

      setCopied(true);

      toast.success("Copied to Clipboard!");

      setTimeout(() => {

        setCopied(false);

      },2000);

    }

    catch{

      toast.error("Copy Failed");

    }

  };

  return (

    <motion.button

      whileHover={{
        scale:1.05
      }}

      whileTap={{
        scale:.95
      }}

      onClick={handleCopy}

      className="copy-btn"

    >

      <AnimatePresence mode="wait">

        {

        copied

        ?

        <motion.div

        key="done"

        initial={{opacity:0,scale:.8}}

        animate={{opacity:1,scale:1}}

        exit={{opacity:0,scale:.8}}

        className="copy-content"

        >

          <FaCheck/>

          Copied

        </motion.div>

        :

        <motion.div

        key="copy"

        initial={{opacity:0,scale:.8}}

        animate={{opacity:1,scale:1}}

        exit={{opacity:0,scale:.8}}

        className="copy-content"

        >

          <FaCopy/>

          Copy

        </motion.div>

        }

      </AnimatePresence>

    </motion.button>

  );

}

export default CopyButton;