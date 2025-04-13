import { useState } from 'react';
import "./ManualRow.css";

export default function ManualRow({manual}){
    return (
        <div className="search-results">
            <a href={manual.manual_url}>
            <label >{manual.title}</label>
            </a>
            <img src={manual.cover_image} alt="Cover Image" class="cover_image"></img>
            <label>{manual.manufacture_date} , {manual.product_num}</label>
            <label>Category: {manual.lego_group}</label>
        </div>
    );
}// {} to acc any variable
//yet to use manual image