const uniqueSlow = (array) => {
    const newArray = [];
    for (let i = 0; i < array.length; i++) {
        const ele = array[i]
        if (!newArray.includes(ele)) {
            newArray.push(ele);
        }
    }
    return newArray;
}

const uniqueFast = (array) => {
    const onlyUniques = new Set(array);
    for (let i = 0; i < array.length; i++) {
        const ele = array[i]
        onlyUniques.add(ele);
    }
    return Array.from(onlyUniques);
}

const randomArray = [];
for (let i = 0; i < 100; i++) {
    const randomNumber = Math.floor(Math.random() * 100);
    randomArray.push(randomNumber);
}

const startSlow = new Date();
console.log(uniqueSlow(randomArray));``
const endSlow = new Date();
console.log(`slow n^2 finished in ${endSlow - startSlow} ms`);

const startFast = new Date();
console.log(uniqueFast(randomArray));
const endFast = new Date();
console.log(`fast n^2 finished in ${endFast - startFast} ms`)