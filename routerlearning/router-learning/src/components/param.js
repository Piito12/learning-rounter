import React from "react";
import Menu from "./menu";
import { useParams } from "react-router-dom";

function PostDetail(){
    const params = useParams();
  return (
    <div>
        <Menu/>
        <h1>post parameter (/:id ) is {params.id}</h1>
  </div> 
  )
  
};


export default PostDetail;
