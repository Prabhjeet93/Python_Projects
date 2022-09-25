//make a button text
const buttonText = document.createTextNode("click ME!");
const button = document.createElement("button");
console.log("Hello!");
const buttonContainer = document.getElementById("button-container");

//attach text to button
button.appendChild(buttonText);

//Set up Event Listener
button.addEventListener('click', () => {
    alert("PWST!");
});

//Attach button to container
buttonContainer.appendChild(button);