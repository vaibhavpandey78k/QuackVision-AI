import UploadVideo from "./pages/UploadVideo";
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <>
      <Toaster
        position="top-right"
        toastOptions={{
          style: {
            background: "#111827",
            color: "#fff",
          },
        }}
      />

      <UploadVideo />
    </>
  );
}

export default App;