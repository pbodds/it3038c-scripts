// const path = require("path");

// const hello = "Hello from Node JS var!"

// console.log(`Printing variable hello: ${hello}`);

// console.log("directory name: " + __dirname);

// console.log("Using PATH module:");
// console.log(`Hello from file ${path.basename(__filename)}`);

// console.log(`Process args: ${process.argv[1]}`)

process.stdout.write("Hello. What is your name? ")

process.stdin.on('data', (data1) => {
  console.log("Hello " + data1.toString())
  process.exit()
});

process.on('exit', () => {
    console.log('Thanks for the info!')
  });