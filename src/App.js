import logo from './logo.svg'; // image .svg format
import './App.css';
import React, {useState, useEffect} from 'react';


function App() { // WILL WRAP <HTML>
  const [currentTime, setCurrentTime] = useState(0);

  useEffect( () => {

    fetch('/api/time').then(result => result.json()).then(data => {
      setCurrentTime(data.time);
    })
  },[]);


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>
          I hope there is snow tomorrow. The current time is {currentTime}
        </p>
      </header>
    </div>
  );
}

export default App;

//entry point (everything starts here)

// React helps code HTML using javascript (intermediate)
//  .js is the mian entrypoint and so then you can load the HTML there insteead od the other way around