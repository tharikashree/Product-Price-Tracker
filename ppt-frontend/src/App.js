import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [email, setEmail] = useState('');
  const [expectedPrice, setExpectedPrice] = useState("");
  const [responseMessage, setResponseMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/check-price", {
        url,
        expected_price: expectedPrice,
        email: email,
      });
      setResponseMessage(response.data.message);
    } catch (error) {
      setResponseMessage("An error occurred. Please try again.");
    }
  };

  return (
    <div className="container"> {/* Added container class */}
      <h1>Amazon Price Tracker</h1>
      <form onSubmit={handleSubmit}>
        <label>Email Address</label>
        <input
          type="email"
          value={email}
          placeholder="Enter your email address"
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <label>Product URL</label>
        <input
          type="text"
          placeholder="Enter the product URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          required
        />
        <label>Expected Price (₹)</label>
        <input
          type="number"
          placeholder="Enter the expected price"
          value={expectedPrice}
          onChange={(e) => setExpectedPrice(e.target.value)}
          required
        />
        <button type="submit">Track Price</button>
      </form>
      {responseMessage && <p>{responseMessage}</p>}
    </div>
  );
}

export default App;