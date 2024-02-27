import react from "react";
import { Route, Routes } from "react-router-dom";
import Home from "./Components/Screens/Home";
import Login from "./Components/Screens/Login";
import "./App.css";

function App() {
  return (
    <>
    <Login/>
    {/* <BrowserRouter>
      <Routes>

        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />

      </Routes>
    </BrowserRouter> */}
    </>
  );
}

export default App;
