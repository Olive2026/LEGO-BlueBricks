 // image .svg format
import { useState } from 'react';
import SearchInput from './SearchInput';
import SearchResults from './SearchResults';



export default function App() { 

  // WILL WRAP <HTML>
  const [total, setTotal] = useState(0);
  const [manuals, setManuals] = useState([
    { cover_image: "", lego_group: "", manual_image: "", manual_url: "", manufacture_date: "", product_num: "", title: "" },
  
  ]);
  const handleSearchChange = (results) => {
    setTotal(results.totals);
    if(results.totals > 0) {
      const newManuals =results.manuals.map(manual => manual);
      setManuals(newManuals);
    }
  }


  return (
    <div>
      <SearchInput textChangeFunction={handleSearchChange} />
      <SearchResults totals={total} manuals={manuals} />
    </div>
  );
  
};



//entry point (everything starts here)

// React helps code HTML using javascript (intermediate)
//  .js is the mian entrypoint and so then you can load the HTML there insteead od the other way around