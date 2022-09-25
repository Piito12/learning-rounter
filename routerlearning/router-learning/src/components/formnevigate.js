import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Menu from "./menu";


function  FormSubmit(){
    const [text , setText] = useState("")

    let handleInput = (e) =>{
        let input = e.target.value
        console.log(input);
        setText(input)
    };

    const nevigate = useNavigate()
    
    const handleSubmit = () =>{
        alert("Your Sunmit Now!!")
        nevigate(`/posts/${text}`);
    }
  return (
    <div>
        <Menu/>
        <h1>Form</h1>
        <form htmlFor="name" onSubmit={handleSubmit}>
            <label>
                name 
                <input type="text" onChange={handleInput} placeholder="Enter your name Here!!"/>
            </label>
            <button type="submit">Log in</button>

        </form>
    </div>
  )  
};

export default FormSubmit;