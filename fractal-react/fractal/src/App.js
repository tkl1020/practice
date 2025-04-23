import React from "react";
import FractalBackground from "./fractal";
import Portfolio from "./portfolio";
import "./App.css";

function App() {
  return (
    <div className="App" style={{ position: "relative", zIndex: 1 }}>
      <FractalBackground />
      <div style={{ position: "relative", zIndex: 2 }}>
        <Portfolio />
      </div>
    </div>
  );
}

export default App;
