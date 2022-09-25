import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/home";
import DashBoard from "./components/dashboard";
import PostDetail from "./components/param";
import FormSubmit from "./components/formnevigate";



function App() {
  
  const NoMatch = () => <h1>404 page NotFound</h1>
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard"  element = {< DashBoard/>} />
        <Route path="/posts/:id" element = {<PostDetail/>}/>
        <Route path ="/submit" element = {<FormSubmit/>} />
        <Route path="*" element = {<NoMatch/>}/>
      </Routes>
    </Router>
  );
}

export default App;

