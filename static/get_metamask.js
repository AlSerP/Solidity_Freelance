const ethereumButton =document.getElementById('register1');

ethereumButton.addEventListener("click", () => {
  //Will Start the metamask extension
  ethereum.enable();
  console.log("TRUE");
});