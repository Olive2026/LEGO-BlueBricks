import { useState } from 'react';
import "./ManualRow.css";

export default function ManualRow({manual}){
    return (
        <div className="manual-row">
            
            <div className='image-container'>
                <img src={manual.cover_image} alt="Cover Image" class="cover_image"></img>
            </div>
            <div className='content'>
                <div className='content-title'>
                    <a href={manual.manual_url}>
                    <label >{manual.title}</label>
                    </a>
                </div>
                <div className='content-text'>
                <span>{manual.manufacture_date} , {manual.product_num}</span>
                <span>Category: {manual.lego_group}</span>
                </div>
            </div>
            
        </div>
    );
}// {} to acc any variable
//yet to use manual image