import React from "react";
import { Link } from "react-router-dom";

const Menu = () =>{
    return(
        <div>
            <Link to = "/">Home page</Link>
            <Link to = "/dashboard">DashBoard</Link>
            <Link to = "/posts/oat">Post Detail 1</Link>
            <Link to = "/posts/pin">Post Detail 2</Link>
            <Link to = "/submit">Submit Name!!</Link>
        </div>
    )
};

export default Menu;