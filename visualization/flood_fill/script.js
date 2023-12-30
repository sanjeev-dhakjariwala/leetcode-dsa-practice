const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const srInput = document.getElementById("sr");
const scInput = document.getElementById("sc");
const colorInput = document.getElementById("color");
const fillButton = document.getElementById("fillButton");

const image = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 1],
]; // Sample image data

// Function to draw the image on the canvas
function drawImage() {
  const width = image[0].length;
  const height = image.length;
  canvas.width = width * 10; // Adjust cell size as needed
  canvas.height = height * 10;

  for (let i = 0; i < height; i++) {
    for (let j = 0; j < width; j++) {
      const color = image[i][j];
      ctx.fillStyle = `rgb(${color}, ${color}, ${color})`;
      ctx.fillRect(j * 10, i * 10, 10, 10); // Adjust cell size accordingly
    }
  }
}

// Flood fill function (recursive)
function floodFill(image, sr, sc, newColor) {
  const oldColor = image[sr][sc];
  if (oldColor !== newColor) {
    image[sr][sc] = newColor;
    // Recursively call for 4 directions
    if (sr > 0) floodFill(image, sr - 1, sc, newColor);
    if (sc > 0) floodFill(image, sr, sc - 1, newColor);
    if (sr < image.length - 1) floodFill(image, sr + 1, sc, newColor);
    if (sc < image[0].length - 1) floodFill(image, sr, sc + 1, newColor);
  }
  drawImage(); // Update the canvas after each fill
}

fillButton.addEventListener("click", () => {
  const sr = parseInt(srInput.value);
  const sc = parseInt(scInput.value);
  const newColor = colorInput.value;
  floodFill(image, sr, sc, newColor);
  console.log(`Button Clicked!!!`)
});

drawImage(); // Draw the initial image
