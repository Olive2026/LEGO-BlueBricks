import { useState } from 'react';
import "./SearchResults.css";
import ManualRow from './ManualRow';

export default function SearchResults({totals, manuals}){

    console.log("total = " + totals);
    return (
        <div className="search-results">
            <label >found {totals} manuals</label>
            {manuals.map(manual => (
                <ManualRow manual={manual}/>
            ))}
        </div>
    );
}