import React, { useEffect } from 'react'; // Добавлен импорт useEffect
import axios from 'axios'; // Добавлен импорт axios
import logo from './logo.svg';
import './App.css';

function App() {
  // Хук useEffect должен быть внутри компонента
  useEffect(() => {
    axios.get('http://localhost:8000/api/test')
      .then(res => console.log(res.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []); // Пустой массив зависимостей означает, что эффект выполнится один раз при монтировании

  interface TestResponse {
    message: string;
  }
  
  useEffect(() => {
    axios.get<TestResponse>('http://localhost:8000/api/test')
      .then(res => console.log(res.data.message))
      .catch(error => console.error('Error:', error));
  }, []);

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
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;