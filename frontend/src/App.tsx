// To start the frontend development server
// cd frontend
// npm install
// npm start

// After that you can make changes here
// and see them reflected in the browser immediately without a refresh

import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { useQuery } from "@tanstack/react-query";

function App() {
  const currentTime = useQuery({
    queryKey: ["currentTime"],
    queryFn: async () => {
      const response = await fetch("get_time");
      const data = await response.json();
      return data.time;
    },
  });

  console.log("Current Time from Backend:", currentTime);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          React Docs
        </a>
        
        {currentTime.data}
      </header>
    </div>
  );
}

export default App;
