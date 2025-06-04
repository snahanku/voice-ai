// src/App.js
import React from "react";
import AudioRecorder from "./components/Audio";

function App() {
  return (
    <div className="App">
      <h1 className="text-xl font-bold p-4">🎙️ Voice-to-Text Demo</h1>
      <AudioRecorder />
    </div>
  );
}

export default App;
