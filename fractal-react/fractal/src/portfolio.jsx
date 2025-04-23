import React from "react";

export default function Portfolio() {
  return (
    <div
      style={{
        color: "#f5f5f5",
        fontFamily: "'Inter', 'Segoe UI', 'Roboto', sans-serif",
        width: "100%",
        padding: 0,
        margin: 0,
      }}
    >
      {/* Hero Section */}
      <section
        style={{
          height: "100vh",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          textAlign: "center",
          padding: "0 10vw",
        }}
      >
        <h1 style={{ fontSize: "4rem", marginBottom: "1rem" }}>Tom Leonard</h1>
        <h2 style={{ fontSize: "2rem", fontWeight: 400, opacity: 0.85 }}>
          Full Stack Developer
        </h2>
        <p
          style={{
            fontSize: "1.25rem",
            marginTop: "2rem",
            maxWidth: "700px",
            lineHeight: "1.8",
            opacity: 0.7,
          }}
        >
          I build modern web applications that balance function and form. From front-end visuals to back-end logic, I code with clarity and deliver with intent.
        </p>
      </section>

      {/* Projects Section Header */}
      <section
        style={{
          height: "100vh",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          padding: "0 10vw",
        }}
      >
        <h2 style={{ fontSize: "3rem", fontWeight: 600, margin: 0 }}>
          Projects
        </h2>
      </section>

      {/* Project 1 */}
      <section
        style={{
          minHeight: "100vh",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          padding: "5vh 10vw",
        }}
      >
        <div style={{ width: "100%", maxWidth: "1000px" }}>
          <h3 style={{ fontSize: "2rem", marginBottom: "1rem" }}>
            Fractal Cursor Effect
          </h3>
          <p
            style={{
              fontSize: "1.1rem",
              lineHeight: "1.8",
              opacity: 0.75,
              marginBottom: "3rem",
              maxWidth: "800px",
            }}
          >
            A custom canvas animation that tracks your cursor and draws fractal
            lines between points. Uses React, the HTML5 canvas API, and math
            magic to create a unique, interactive background.
          </p>
          <div
            style={{
              backgroundColor: "#1a1a1a",
              width: "100%",
              height: "400px",
              borderRadius: "12px",
              border: "1px solid #333",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "#777",
              fontStyle: "italic",
            }}
          >
            [ Live preview / screenshot placeholder ]
          </div>
        </div>
      </section>

      {/* Additional projects can follow same format */}
      <section
        style={{
          minHeight: "100vh",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          padding: "5vh 10vw",
        }}
      >
        <div style={{ width: "100%", maxWidth: "1000px" }}>
          <h3 style={{ fontSize: "2rem", marginBottom: "1rem" }}>
            SQLite Faker Generator
          </h3>
          <p
            style={{
              fontSize: "1.1rem",
              lineHeight: "1.8",
              opacity: 0.75,
              marginBottom: "3rem",
              maxWidth: "800px",
            }}
          >
            A Python-powered tool that generates random user data with the
            Faker library and inserts it into a ready-to-use `.db` file. Great
            for testing and demoing SQL skills.
          </p>
          <div
            style={{
              backgroundColor: "#1a1a1a",
              width: "100%",
              height: "400px",
              borderRadius: "12px",
              border: "1px solid #333",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "#777",
              fontStyle: "italic",
            }}
          >
            [ Live preview / screenshot placeholder ]
          </div>
        </div>
      </section>
    </div>
  );
}
