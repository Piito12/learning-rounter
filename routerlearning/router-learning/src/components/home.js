import React, { useEffect, useState } from "react";
import Menu from "./menu";


const Home = () =>{
    const [loading, setLoading] = useState(null)    
    
    useEffect(()=>{
        
        getloading()
        
        
        setTimeout(()=>{
            setLoading(null)
        },3000)        
    },[])

    const getloading = () =>{
        setLoading("Loading")
    };
    return  (
        
        <div>
            {loading === "Loading" ?(
                <h1>Loading ...</h1>
            )
            :(<div>
                {<Menu/>}
                <h1>Home page</h1>
                </div>)
            }
        </div>
    )
}

export default Home;