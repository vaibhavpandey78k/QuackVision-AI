import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import "./Styles/Global.css";
import "./Styles/upload.css";
import "./Styles/dashboard.css";
import "./Styles/videopreview.css";
import "./Styles/processing.css";
import "./Styles/insights.css";
import "./Styles/caption.css";
import "./Styles/copybuttons.css";
import "./Styles/download.css";

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
