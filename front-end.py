import React, { useState, useEffect } from "react";

const FoodNutrients = () => {
  const [foodName, setFoodName] = useState("");
  const [nutrients, setNutrients] = useState([]);

  useEffect(() => {
    fetch("/api/food-nutrients")
      .then((response) => response.json())
      .then((data) => {
        setNutrients(data);
      });
  }, []);

  const handleFoodNameChange = (event) => {
    setFoodName(event.target.value);
  };

  const renderNutrients = () => {
    if (!nutrients) {
      return null;
    }

    return nutrients.map((nutrient) => {
      const { foodName, carbohydrates, protein, fat, fiber, vitaminC, potassium, expireDate } = nutrient;

      return (
        <div key={foodName}>
          <h2>{foodName}</h2>
          <ul>
            <li>Carbohydrates: {carbohydrates}</li>
            <li>Protein: {protein}</li>
            <li>Fat: {fat}</li>
            <li>Fiber: {fiber}</li>
            <li>Vitamin C: {vitaminC}</li>
            <li>Potassium: {potassium}</li>
            <li>Expire Date: {expireDate}</li>
          </ul>
        </div>
      );
    });
  };

  return (
    <div>
      <h1>Food Nutrients</h1>
      <input
        type="text"
        placeholder="Enter food name"
        onChange={handleFoodNameChange}
      />
      <button onClick={() => {
        setNutrients(
          nutrients.filter((nutrient) => nutrient.foodName === foodName)
        );
      }}>
        Search
      </button>
      {renderNutrients()}
    </div>
  );
};

export default FoodNutrients;