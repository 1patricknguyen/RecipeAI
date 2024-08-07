"use client";
import React, { useState } from "react";
import { Input } from "@/components/ui/input";

export default function Frontpage() {
  const [formData, setFormData] = useState({
    ingredients: ""
  });
  const [responseData, setResponseData] = useState(null);
  const [linkData, setLinkData] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e, endpoint) => {
    e.preventDefault();
    setLinkData(null);
    setResponseData(null);
    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
      });
      const data = await response.json();
      if (endpoint.includes("link")) {
        setLinkData(data);
        console.log(data);
      } else {
        setResponseData(data);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="flex flex-col items-center w-full max-w-md gap-4">
      <div className="flex items-center w-full">
        <Input
          type="text"
          name="ingredients"
          value={formData.ingredients}
          onChange={handleChange}
          placeholder="Enter ingredients (e.g. 'tomato, onion, garlic')..."
          className="w-full"
        />
      </div>
      <div className="flex w-full gap-4">
        <button
          className="flex-1 inline-flex items-center justify-center rounded-md border border-transparent bg-primary px-4 py-2 text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-primary/80 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2"
          onClick={(e) => handleSubmit(e, "http://127.0.0.1:5000/api/recipe")}
        >
          Generate recipe
        </button>
        <button
          className="flex-1 inline-flex items-center justify-center rounded-md border border-input bg-background px-4 py-2 text-sm font-medium shadow-sm transition-colors hover:bg-accent hover:text-accent-foreground focus:outline-none focus:ring-1 focus:ring-ring"
          onClick={(e) => handleSubmit(e, "http://127.0.0.1:5000/api/link")}
        >
          Get existing recipes
        </button>
      </div>
      {responseData && (
  <div className="mt-4 p-4 border rounded-md w-full bg-white shadow-lg">
    <h2 className="text-xl font-semibold mb-4">{responseData.title}</h2>

    <div className="mb-4">
      <h3 className="text-lg font-medium mb-2">Ingredients:</h3>
      <ul className="list-disc list-inside">
        {responseData.ingredients.map((ingredient, index) => (
          <li key={index} className="mb-1 text-gray-800">
            {ingredient}
          </li>
        ))}
      </ul>
    </div>

    <div>
      <h3 className="text-lg font-medium mb-2">Steps:</h3>
      <ol className="list-decimal list-inside">
        {responseData.steps.map((step, index) => (
          <li key={index} className="mb-2 text-gray-800">
            {step}
          </li>
        ))}
      </ol>
    </div>
  </div>
)}
      {linkData && (
        <div className="mt-4 p-4 border rounded-md w-full">
          <h2 className="text-lg font-semibold">Links:</h2>
          {linkData.links ? (
            linkData.links.map((link, index) => (
              <div key={index} className="mb-4">
                <h3 className="text-md font-bold">{link.title}</h3>
                <p><strong>URL:</strong> <a href={link.link} target="_blank" rel="noopener noreferrer">{link.link}</a></p>
              </div>
            ))
          ) : (
            <p>No links found.</p>
          )}
        </div>
      )}

    </div>
  );
}