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