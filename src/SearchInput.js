import React, { useRef } from "react";
import axios from 'axios';

import "./SearchInput.css";

export default function SearchInput({textChangeFunction}) {
    const inputRef = useRef(null);
    const handleClick = () => {
        console.log(inputRef.current.value);
        // call backhand
        let query = {
            keyword:inputRef.current.value
        }
        let manuals = [];
        axios.post("http://localhost:8080/api/search", query).then(response => {
            manuals = response.data;
            console.log(manuals);
            textChangeFunction(manuals);
        }).catch(error => {
            console.log(error);
        });
        // call textChange(info)
        
        
        
    };

    return (
        <div className="component-search-input">
            <div>
                <label >Enter your manual keyword to search </label>
                <input id="search_query" ref={inputRef}/>
                <button onClick={handleClick}>Search</button>
            </div>
        </div>
    );
}


//npm start ofr quick start opens in browser