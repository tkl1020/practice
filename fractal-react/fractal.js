import React, { useEffect, useRef } from "react";

export default function FractalCursorEffect() { const canvasRef = useRef(null);

useEffect(() => { const canvas = canvasRef.current; const ctx = canvas.getContext("2d"); canvas.width = window.innerWidth; canvas.height = window.innerHeight;

let mouseX = -100;
let mouseY = -100;

function drawFractal(x1, y1, x2, y2, depth) {
  if (depth === 0) {
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    return;
  }

  const midX = (x1 + x2) / 2 + (Math.random() - 0.5) * 20;
  const midY = (y1 + y2) / 2 + (Math.random() - 0.5) * 20;

  drawFractal(x1, y1, midX, midY, depth - 1);
  drawFractal(midX, midY, x2, y2, depth - 1);
}

function draw() {
  ctx.fillStyle = "#000033"; // Deep blue background
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.strokeStyle = "#ffffff";
  ctx.lineWidth = 1;

  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;

  for (let i = 0; i < 10; i++) {
    const angle = (i / 10) * Math.PI * 2;
    const endX = centerX + Math.cos(angle) * 150;
    const endY = centerY + Math.sin(angle) * 150;
    drawFractal(endX, endY, mouseX, mouseY, 4);
  }
}

function animate() {
  draw();
  requestAnimationFrame(animate);
}

animate();

const updateMouse = (e) => {
  mouseX = e.clientX;
  mouseY = e.clientY;
};

window.addEventListener("mousemove", updateMouse);

return () => {
  window.removeEventListener("mousemove", updateMouse);
};

}, []);

return <canvas ref={canvasRef} style={{ display: "block" }} />; }