// function x() {
//   for (let i = 1; i <= 5; i++) {
//     setTimeout(function () {
//       console.log(i);
//     }, i * 1000);
//   }
//   console.log("Namasthey have");
// }
// x();

function x() {
  for (var i = 1; i <= 5; i++) {
    function close(x) {
      setTimeout(function () {
        console.log(x);
      }, x * 1000);
    }
    close(i);
  }
  console.log("Namasthey have");
}
x();

function swap() {
  let a = 7;
  let b = 8;
  // with using third variable:
  //   let temp = a;
  //   a = b;
  //   b = temp;
  // without using third variable:
  // array destructuring:
  [a, b] = [b, a];
  console.log(a, b);
}
swap();
arr = [1, 1, 2, 3, 4, 5, 4, 4, 3];
// find duplicates in array:
const duplicates = arr.filter((ele, index) => arr.indexOf(ele) !== index);
const newarr = arr.filter((ele, index) => arr.indexOf(ele) === index);

console.log(duplicates);
console.log(newarr);
let arr = ["apple", "mango", "apple", "orange", "mango", "mango"];

function removeDuplicates(arr) {
  let unique = [];
  arr.forEach((element) => {
    if (!unique.includes(element)) {
      unique.push(element);
    }
  });
  return unique;
}
console.log(removeDuplicates(arr));
arr = [1, 1, 2, 3, 4, 5, 4, 4, 3];

const dup = arr.forEach((ele) => {
  return ele + 2;
});
console.log(dup);

// reverse arr:
const reverseA = (arr) => {
  newl = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    newl.push(arr[i]);
  }
  return newl;
};
arr = [1, 2, 3, 4];
console.log(reverseA(arr));
// reverse string:
const reverseS = (str) => {
  newl = [];
  for (let i = str.length - 1; i >= 0; i--) {
    newl.push(str[i]);
  }
  return newl.join("");
};
console.log(reverseS("VERSION"));

// remove dupl in str:
const dupli = (str) => {
  let unormap = new Map();
  let s = "";
  for (let i = 0; i < str.length; i++) {
    if (!unormap.has(str[i])) {
      s += str[i];
      unormap.set(str[i], 1);
    }
  }
  return s;
};

console.log(dupli("ggffgghs"));
